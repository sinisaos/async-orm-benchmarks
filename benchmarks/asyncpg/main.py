from contextlib import asynccontextmanager
from decimal import Decimal

import orjson
from config import database
from fastapi import FastAPI
from fastapi.responses import JSONResponse


def decimal_serializer(obj) -> float:
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Type not serializable")


class ORJSONResponse(JSONResponse):
    def render(self, content):
        return orjson.dumps(content, default=decimal_serializer)


def json_converter(data: dict) -> dict:
    for k, v in data.items():
        if k.startswith("json_") or k.startswith("question_"):
            data[k] = orjson.loads(v)
    return data


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get("/small-table/")
async def tags_list() -> ORJSONResponse:
    query = "SELECT * FROM tag LIMIT 50"
    async with database.pool.acquire() as connection:
        rows = await connection.fetch(query)
        return ORJSONResponse([dict(row) for row in rows])


@app.get("/small-table/{pk:int}/")
async def tag_single(pk: int) -> ORJSONResponse:
    query = "SELECT * FROM tag WHERE id = $1"
    async with database.pool.acquire() as connection:
        row = await connection.fetchrow(query, pk)
        return ORJSONResponse(dict(row))


@app.get("/related-table/")
async def questions_list() -> ORJSONResponse:
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
    async with database.pool.acquire() as connection:
        rows = await connection.fetch(query)
        return ORJSONResponse([json_converter(dict(row)) for row in rows])


@app.get("/related-table/{pk:int}/")
async def question_single(pk: int) -> ORJSONResponse:
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
        WHERE q.id = $1
        GROUP BY q.id, u.id
    """
    async with database.pool.acquire() as connection:
        row = dict(await connection.fetchrow(query, pk))
        return ORJSONResponse(json_converter(row))


@app.get("/mega-table/")
async def mega_table_list() -> ORJSONResponse:
    query = "SELECT * FROM mega_table LIMIT 50"
    async with database.pool.acquire() as connection:
        rows = await connection.fetch(query)
        return ORJSONResponse([json_converter(dict(row)) for row in rows])


@app.get("/mega-table/{pk:int}/")
async def mega_table_single(pk: int) -> ORJSONResponse:
    query = "SELECT * FROM mega_table WHERE id = $1"
    async with database.pool.acquire() as connection:
        row = dict(await connection.fetchrow(query, pk))
        return ORJSONResponse(json_converter(row))
