from contextlib import asynccontextmanager
from decimal import Decimal

import orjson
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool


def decimal_serializer(obj) -> float:
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Type not serializable")


class ORJSONResponse(JSONResponse):
    def render(self, content):
        return orjson.dumps(content, default=decimal_serializer)


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_pool = AsyncConnectionPool(
        conninfo="postgres://postgres:postgres@localhost:5432/perfdb",
        max_size=10,
        open=False,
    )
    app.state.db_pool = db_pool
    await db_pool.open()
    yield
    await db_pool.close()


app = FastAPI(lifespan=lifespan)


@app.get("/small-table/")
async def tags_list(request: Request) -> ORJSONResponse:
    query = "SELECT * FROM tag LIMIT 50"
    async with request.app.state.db_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query)
            results = await cur.fetchall()
            return ORJSONResponse(results)


@app.get("/small-table/{pk:int}/")
async def tag_single(request: Request, pk: int) -> ORJSONResponse:
    query = "SELECT * FROM tag WHERE id = %s"
    async with request.app.state.db_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, [pk])
            result = await cur.fetchone()
            return ORJSONResponse(result)


@app.get("/related-table/")
async def questions_list(request: Request) -> ORJSONResponse:
    query = """
        SELECT q.*,
            JSONB_BUILD_OBJECT(
                'id', u.id,
                'username', u.username,
                'email', u.email,
                'superuser', u.superuser
            ) question_user,
            ARRAY_TO_JSON(
                ARRAY_REMOVE(
                    ARRAY_AGG(DISTINCT t), NULL)
                ) question_tags
        FROM question q
        LEFT JOIN base_user u ON q.user_id = u.id
        LEFT JOIN question_tag qt ON qt.question_id = q.id
        LEFT JOIN tag t ON t.id = qt.tag_id
        GROUP BY q.id, u.id
        ORDER BY q.id
        LIMIT 50
        """
    async with request.app.state.db_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query)
            results = await cur.fetchall()
            return ORJSONResponse(results)


@app.get("/related-table/{pk:int}/")
async def question_single(request: Request, pk: int) -> ORJSONResponse:
    query = """
        SELECT q.*,
            JSONB_BUILD_OBJECT(
                'id', u.id,
                'username', u.username,
                'email', u.email,
                'superuser', u.superuser
            ) question_user,
            ARRAY_TO_JSON(
                ARRAY_REMOVE(
                    ARRAY_AGG(DISTINCT t), NULL)
            ) question_tags,
            ARRAY_TO_JSON(
                ARRAY_REMOVE(
                    ARRAY_AGG(DISTINCT a), NULL)
            ) question_answers
        FROM question q
        JOIN base_user u ON q.user_id = u.id
        LEFT JOIN question_tag qt ON qt.question_id = q.id
        LEFT JOIN tag t ON t.id = qt.tag_id
        LEFT JOIN answer a ON a.question_id = q.id
        WHERE q.id = %s
        GROUP BY q.id, u.id
    """
    async with request.app.state.db_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, [pk])
            result = await cur.fetchone()
            return ORJSONResponse(result)


@app.get("/mega-table/")
async def mega_table_list(
    request: Request,
) -> ORJSONResponse:
    query = "SELECT * FROM mega_table LIMIT 50"
    async with request.app.state.db_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query)
            results = await cur.fetchall()
            return ORJSONResponse(results)


@app.get("/mega-table/{pk:int}/")
async def mega_table_single(request: Request, pk: int) -> ORJSONResponse:
    query = "SELECT * FROM mega_table WHERE id = %s"
    async with request.app.state.db_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, [pk])
            result = await cur.fetchone()
            return ORJSONResponse(result)
