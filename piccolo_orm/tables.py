import decimal
from datetime import datetime

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
from piccolo.engine.postgres import PostgresEngine
from piccolo.table import Table

DB = PostgresEngine(
    config={
        "database": "perfdb",
        "user": "postgres",
        "password": "postgres",
        "host": "localhost",
        "port": 5432,
    }
)


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
    varchar_col_1 = Varchar(max_length=255, default="value1")
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
    varchar_col_2 = Varchar(max_length=255, default="value1")
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
    varchar_col_3 = Varchar(max_length=255, default="value1")
    text_col_3 = Text(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_3 = Numeric(digits=(5, 2), default=decimal.Decimal("2.2"))
    json_col_3 = JSON(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}
    )


async def open_database_connection_pool():
    try:
        await DB.start_connection_pool(max_size=10)
    except Exception:
        print("Unable to connect to the database")


async def close_database_connection_pool():
    try:
        await DB.close_connection_pool()
    except Exception:
        print("Unable to connect to the database")
