import pathlib
from decimal import Decimal

import orjson
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import (
    MegaTable,
    Question,
    Tag,
)
from oxyde import PoolSettings, db

CURRENT_DIR = pathlib.Path(__file__).parent.resolve()
PROJECT_ROOT = CURRENT_DIR.parents[1]
DATABASE_PATH = PROJECT_ROOT / "benchmark.db"


def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Type not serializable")


class ORJSONResponse(JSONResponse):
    def render(self, content):
        return orjson.dumps(content, default=decimal_serializer)


app = FastAPI(
    lifespan=db.lifespan(
        default=f"sqlite://{DATABASE_PATH}",
        settings=PoolSettings(
            sqlite_journal_mode="WAL",
            # Balance between speed and safety
            sqlite_synchronous="NORMAL",
            # Lock timeout in milliseconds
            sqlite_busy_timeout=60000,
        ),
    )
)


@app.get("/small-table/")
async def tags_list() -> ORJSONResponse:
    data = await Tag.objects.limit(50).all()
    return ORJSONResponse([d.model_dump() for d in data])


@app.get("/small-table/{pk:int}/")
async def tag_single(pk: int) -> ORJSONResponse:
    data = await Tag.objects.filter(id=pk).first()
    return ORJSONResponse(data.model_dump())


@app.get("/related-table/")
async def questions_list() -> ORJSONResponse:
    data = await Question.objects.join("user").prefetch("tags").limit(50).all()
    return ORJSONResponse([d.model_dump() for d in data])


@app.get("/related-table/{pk:int}/")
async def question_single(pk: int) -> ORJSONResponse:
    question_data = (
        await Question.objects.filter(id=pk)
        .join("user")
        .prefetch("tags", "answers")
        .first()
    )
    return ORJSONResponse(question_data.model_dump())


@app.get("/mega-table/")
async def mega_table_list() -> ORJSONResponse:
    data = await MegaTable.objects.limit(50).all()
    return ORJSONResponse([d.model_dump() for d in data])


@app.get("/mega-table/{pk:int}/")
async def mega_table_single(pk: int) -> ORJSONResponse:
    data = await MegaTable.objects.filter(id=pk).first()
    return ORJSONResponse(data.model_dump())
