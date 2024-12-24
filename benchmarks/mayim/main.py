from decimal import Decimal
from typing import List

import orjson
from mayim import PostgresExecutor
from mayim.extension import StarletteMayimExtension
from models import MegaTableModel, QuestionModel, SingleQuestionModel, TagModel
from psycopg_pool import AsyncConnectionPool
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


def decimal_serializer(obj) -> float:
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Type not serializable")


class ORJSONResponse(JSONResponse):
    def render(self, content):
        return orjson.dumps(content, default=decimal_serializer)


class TagExecutor(PostgresExecutor):
    async def select_all_tags(  # type: ignore[empty-body]
        self,
        limit: int = 50,
    ) -> List[TagModel]: ...
    async def select_single_tag(self, pk: int) -> TagModel: ...


class QuestionExecutor(PostgresExecutor):
    async def select_all_questions(  # type: ignore[empty-body]
        self,
        limit: int = 50,
    ) -> List[QuestionModel]: ...
    async def select_single_question(self, pk: int) -> SingleQuestionModel: ...


class MegaTableExecutor(PostgresExecutor):
    async def select_all_mega_tables(  # type: ignore[empty-body]
        self,
        limit: int = 50,
    ) -> List[MegaTableModel]: ...
    async def select_single_mega_table(self, pk: int) -> MegaTableModel: ...


ext = StarletteMayimExtension(
    executors=[TagExecutor, QuestionExecutor, MegaTableExecutor],
)

# the only way I can find to set connection pool like in other benchmarks
ext.mayim_kwargs["pool"] = AsyncConnectionPool(
    conninfo="postgres://postgres:postgres@localhost:5432/perfdb",
    max_size=10,
)


async def tags_list(_: Request):
    executor = TagExecutor()
    data = await executor.select_all_tags()
    return ORJSONResponse([dict(item) for item in data])


async def tag_single(request: Request):
    pk = request.path_params.get("pk", None)
    executor = TagExecutor()
    data = await executor.select_single_tag(pk=pk)
    return ORJSONResponse(dict(data))


async def questions_list(_: Request):
    executor = QuestionExecutor()
    data = await executor.select_all_questions()

    return ORJSONResponse([dict(item) for item in data])


async def question_single(request: Request):
    pk = request.path_params.get("pk", None)
    executor = QuestionExecutor()
    data = await executor.select_single_question(pk=pk)
    return ORJSONResponse(dict(data))


async def mega_table_list(_: Request):
    executor = MegaTableExecutor()
    data = await executor.select_all_mega_tables()
    return ORJSONResponse([dict(item) for item in data])


async def mega_table_single(request: Request):
    pk = request.path_params.get("pk", None)
    executor = MegaTableExecutor()
    data = await executor.select_single_mega_table(pk=pk)
    return ORJSONResponse(dict(data))


app = Starlette(
    routes=[
        Route("/small-table/", tags_list),
        Route("/small-table/{pk:int}/", tag_single),
        Route("/related-table/", questions_list),
        Route("/related-table/{pk:int}/", question_single),
        Route("/mega-table/", mega_table_list),
        Route("/mega-table/{pk:int}/", mega_table_single),
    ],
)
ext.init_app(app)
