from contextlib import asynccontextmanager
from decimal import Decimal

import orjson
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from tables import (
    Answer,
    MegaTable,
    Question,
    Tag,
    close_database_connection_pool,
    open_database_connection_pool,
)


def decimal_serializer(obj) -> float:
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Type not serializable")


class ORJSONResponse(JSONResponse):
    def render(self, content):
        return orjson.dumps(content, default=decimal_serializer)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await open_database_connection_pool()
    yield
    await close_database_connection_pool()


app = FastAPI(lifespan=lifespan)


@app.get("/small-table/")
async def tags_list() -> ORJSONResponse:
    data = await Tag.select().limit(50)
    return ORJSONResponse(data)


@app.get("/small-table/{pk:int}/")
async def tag_single(pk: int) -> ORJSONResponse:
    data = await Tag.select().where(Tag._meta.primary_key == pk).first()
    return ORJSONResponse(data)


@app.get("/related-table/")
async def questions_list() -> ORJSONResponse:
    data = (
        await Question.select(
            Question.all_columns(),
            Question.user_id.all_columns(),
            Question.tags(),
        )
        .limit(50)
        .output(nested=True)
    )
    return ORJSONResponse(data)


@app.get("/related-table/{pk:int}/")
async def question_single(pk: int) -> ORJSONResponse:
    data = (
        await Question.select(
            Question.all_columns(),
            Question.user_id.all_columns(),
            Question.tags(),
        )
        .where(Question._meta.primary_key == pk)
        .first()
        .output(nested=True)
    )
    question_answers = (
        await Answer.select()
        .where(Answer.question_id == pk)
        .order_by(Answer._meta.primary_key, ascending=False)
    )
    data["question_answers"] = question_answers
    return ORJSONResponse(data)


@app.get("/mega-table/")
async def mega_table_list() -> ORJSONResponse:
    data = await MegaTable.select().limit(50).output(load_json=True)
    return ORJSONResponse(data)


@app.get("/mega-table/{pk:int}/")
async def mega_table_single(pk: int) -> ORJSONResponse:
    data = (
        await MegaTable.select()
        .where(MegaTable._meta.primary_key == pk)
        .first()
        .output(load_json=True)
    )
    return ORJSONResponse(data)
