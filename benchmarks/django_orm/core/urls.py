import typing as t

import orjson
from app.models import Answer, MegaTable, Question, Tag
from django.urls import path
from ninja import NinjaAPI
from ninja.orm import create_schema
from ninja.parser import Parser


class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)


api = NinjaAPI(parser=ORJSONParser())

TagModel: t.Any = create_schema(Tag)
QuestionModel: t.Any = create_schema(Question, depth=1)
MegaTableModel: t.Any = create_schema(MegaTable)
AnswerModel: t.Any = create_schema(Answer)


class SingleQuestionModel(QuestionModel):
    question_answers: t.List[AnswerModel]


@api.get("/small-table/", response=t.List[TagModel])
async def tags_list(request):
    data = [item async for item in Tag.objects.all()]
    return data[:50]


@api.get("/small-table/{pk}/", response=TagModel)
async def tag_single(request, pk: int):
    data = await Tag.objects.aget(id=pk)
    return data


@api.get("/related-table/", response=t.List[QuestionModel])
async def questions_list(request):
    data = [
        item
        async for item in Question.objects.prefetch_related(
            "user",
            "tags",
        ).all()
    ]
    return data[:50]


@api.get("/related-table/{pk}/", response=SingleQuestionModel)
async def question_single(request, pk: int):
    data = await Question.objects.prefetch_related(
        "user",
        "tags",
        "question_answers",
    ).aget(id=pk)
    return data


@api.get("/mega-table/", response=t.List[MegaTableModel])
async def mega_table_list(request):
    data = [item async for item in MegaTable.objects.all()]
    return data[:50]


@api.get("/mega-table/{pk}/", response=MegaTableModel)
async def mega_table_single(request, pk: int):
    data = await MegaTable.objects.aget(id=pk)
    return data


urlpatterns = [
    path("", api.urls),
]
