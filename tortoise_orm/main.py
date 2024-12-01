from contextlib import asynccontextmanager
from decimal import Decimal

import orjson
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import MegaTable, Question, Tag
from tortoise import Tortoise, connections


def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Type not serializable")


class ORJSONResponse(JSONResponse):
    def render(self, content):
        return orjson.dumps(content, default=decimal_serializer)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await Tortoise.init(
        db_url="postgres://postgres:postgres@localhost:5432/perfdb",
        modules={"models": ["models"]},
    )
    yield
    await connections.close_all()


app = FastAPI(lifespan=lifespan)


@app.get("/small-table/")
async def tags_list() -> ORJSONResponse:
    data = await Tag.all().limit(50).values()
    return ORJSONResponse(data)


@app.get("/small-table/{pk:int}/")
async def tag_single(pk: int) -> ORJSONResponse:
    data = await Tag.filter(id=pk).first().values()
    return ORJSONResponse(data)


@app.get("/related-table/")
async def questions_list() -> ORJSONResponse:
    data = await Question.all().prefetch_related("user", "tags").limit(50)
    return ORJSONResponse([dict(row) for row in data])


@app.get("/related-table/{pk:int}/")
async def question_single(pk: int) -> ORJSONResponse:
    data = (
        await Question.filter(id=pk)
        .prefetch_related("user", "tags")
        .first()
        .values()
    )
    return ORJSONResponse(data)


@app.get("/mega-table/")
async def mega_table_list() -> ORJSONResponse:
    data = await MegaTable.all().limit(50).values()
    return ORJSONResponse(data)


@app.get("/mega-table/{pk:int}/")
async def mega_table_single(pk: int) -> ORJSONResponse:
    data = await MegaTable.filter(id=pk).first().values()
    return ORJSONResponse(data)


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)
