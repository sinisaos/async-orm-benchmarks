import asyncio
import decimal
import pathlib
import sys
from datetime import datetime
from typing import Any, Optional

import aiosqlite
from piccolo.columns.column_types import (
    JSON,
    BigInt,
    Boolean,
    Float,
    ForeignKey,
    Integer,
    LazyTableReference,
    Numeric,
    SmallInt,
    Text,
    Timestamptz,
    Varchar,
)
from piccolo.columns.m2m import M2M
from piccolo.engine.sqlite import SQLiteEngine, dict_factory
from piccolo.table import Table

CURRENT_DIR = pathlib.Path(__file__).parent.resolve()
PROJECT_ROOT = CURRENT_DIR.parents[1]
DATABASE_PATH = PROJECT_ROOT / "benchmark.db"

# Complete isolation of cli tools and migrations
IS_PICCOLO_CLI = (
    any("piccolo" in arg for arg in sys.argv) or "migrations" in sys.argv
)


class SharedSQLiteEngine(SQLiteEngine):
    """
    Custom SQLiteEngine with shared connection
    for better read and write performance
    """

    def __init__(self, path: str, *args, **kwargs):
        super().__init__(path, *args, **kwargs)
        self._shared_connection: Optional[aiosqlite.Connection] = None
        # For locking simultaneous opening of the file itself
        self._lock = asyncio.Lock()

    async def _get_shared_connection(self) -> aiosqlite.Connection:
        if self._shared_connection is None:
            async with self._lock:
                conn = await aiosqlite.connect(**self.connection_kwargs)
                # Adding useful PRAGMA's
                await conn.execute("PRAGMA journal_mode=WAL;")
                await conn.execute("PRAGMA synchronous=NORMAL;")
                self._shared_connection = conn
        return self._shared_connection

    async def _run_in_new_connection(
        self,
        query: str,
        args: Optional[list[Any]] = None,
        query_type: str = "generic",
        table: Optional[type[Table]] = None,
    ):
        if args is None:
            args = []

        # Shared connection
        connection = await self._get_shared_connection()
        connection.row_factory = dict_factory  # type: ignore

        # When we do SELECT queries, we isolate execution directly
        # at the SQLite level without calling commit() and
        # without messing with Piccolo transaction
        if query_type == "generic":
            async with connection.execute(query, args) as cursor:
                return await cursor.fetchall()
        else:
            # For rest query_type operations we keep the standard
            # FK PRAGMA and calling commit()
            await connection.execute("PRAGMA foreign_keys = 1")
            async with connection.execute(query, args) as cursor:
                await connection.commit()
                if query_type == "insert" and self.get_version_sync() < 3.35:
                    assert table is not None
                    pk = await self._get_inserted_pk(cursor, table)
                    return [{table._meta.primary_key._meta.db_column_name: pk}]
                else:
                    return await cursor.fetchall()

    async def close_shared_connection(self):
        if self._shared_connection is not None:
            await self._shared_connection.close()
            self._shared_connection = None


# For migrations and CLI commands we use the standard SQLiteEngine
# and SharedSQLiteEngine for everything else for better performance
if IS_PICCOLO_CLI:
    DB = SQLiteEngine(path=f"{DATABASE_PATH}")
else:
    DB = SharedSQLiteEngine(path=f"{DATABASE_PATH}", timeout=60)


class BaseUser(Table, db=DB):
    username = Varchar()
    email = Varchar()
    superuser = Boolean(default=False)


class Question(Table, db=DB):
    title = Varchar()
    content = Text()
    created_at = Timestamptz()
    updated_at = Timestamptz(auto_update=datetime.now)
    views = Integer()
    likes = Integer()
    user_id = ForeignKey(references=BaseUser)
    tags = M2M(LazyTableReference("QuestionTag", module_path=__name__))


class Tag(Table, db=DB):
    name = Varchar()
    questions = M2M(LazyTableReference("QuestionTag", module_path=__name__))


class Answer(Table, db=DB):
    content = Text()
    created_at = Timestamptz()
    updated_at = Timestamptz(auto_update=datetime.now)
    likes = Integer()
    user_id = ForeignKey(references=BaseUser)
    question_id = ForeignKey(references=Question)


# This is our joining table:
class QuestionTag(Table, db=DB):
    question_id = ForeignKey(Question)
    tag_id = ForeignKey(Tag)


class MegaTable(Table, db=DB):
    float_col_1 = Float(default=2.2)
    smallint_col_1 = SmallInt(default=2)
    integer_col_1 = Integer(default=2000000)
    bigint_col_1 = BigInt(default=99999999)
    varchar_col_1 = Varchar(length=255, default="value1")
    text_col_1 = Text(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_1 = Numeric(digits=(5, 2), default=decimal.Decimal("2.2"))
    json_col_1 = JSON(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}
    )

    float_col_2 = Float(default=2.2)
    smallint_col_2 = SmallInt(default=2)
    integer_col_2 = Integer(default=2000000)
    bigint_col_2 = BigInt(default=99999999)
    varchar_col_2 = Varchar(length=255, default="value1")
    text_col_2 = Text(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_2 = Numeric(digits=(5, 2), default=decimal.Decimal("2.2"))
    json_col_2 = JSON(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}
    )

    float_col_3 = Float(default=2.2)
    smallint_col_3 = SmallInt(default=2)
    integer_col_3 = Integer(default=2000000)
    bigint_col_3 = BigInt(default=99999999)
    varchar_col_3 = Varchar(length=255, default="value1")
    text_col_3 = Text(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_3 = Numeric(digits=(5, 2), default=decimal.Decimal("2.2"))
    json_col_3 = JSON(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}
    )
