from contextlib import asynccontextmanager
from decimal import Decimal

import orjson
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from prisma import Prisma

DB = Prisma()


def custom_serializer(obj) -> float:
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, object):
        return dict(obj)  # type: ignore
    raise TypeError("Type not serializable")


class ORJSONResponse(JSONResponse):
    def render(self, content):
        return orjson.dumps(content, default=custom_serializer)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await DB.connect()
    yield
    if DB.is_connected():
        await DB.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get("/small-table/")
async def tags_list() -> ORJSONResponse:
    data = await DB.tag.find_many(take=50)
    return ORJSONResponse(
        [dict({k: v for k, v in row if v is not None}) for row in data]
    )


@app.get("/small-table/{pk:int}/")
async def tag_single(pk: int) -> ORJSONResponse:
    data = await DB.tag.find_first(where={"id": pk})
    return ORJSONResponse({k: v for k, v in data if v is not None})


@app.get("/related-table/")
async def questions_list() -> ORJSONResponse:
    data = await DB.question.find_many(
        include={"question_tag": True, "base_user": True}, take=50
    )
    return ORJSONResponse([dict(row) for row in data])


@app.get("/related-table/{pk:int}/")
async def question_single(pk: int) -> ORJSONResponse:
    data = await DB.question.find_first(
        include={"question_tag": True, "base_user": True, "answer": True},
        where={"id": pk},
    )
    return ORJSONResponse(data)


@app.get("/mega-table/")
async def mega_table_list() -> ORJSONResponse:
    data = await DB.mega_table.find_many(take=50)
    return ORJSONResponse([dict(row) for row in data])


@app.get("/mega-table/{pk:int}/")
async def mega_table_single(pk: int) -> ORJSONResponse:
    data = await DB.mega_table.find_first(where={"id": pk})
    return ORJSONResponse(data)
