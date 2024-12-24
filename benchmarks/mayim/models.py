import typing as t
from datetime import datetime

from pydantic import BaseModel


class TagModel(BaseModel):
    id: int
    name: str


class QuestionModel(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    views: int
    likes: int
    question_user: t.Dict[str, t.Any]
    question_tags: t.List[t.Dict[str, t.Any]]


class SingleQuestionModel(QuestionModel):
    question_answers: t.List[t.Dict[str, t.Any]]


class MegaTableModel(BaseModel):
    id: int
    float_col_1: float
    smallint_col_1: int
    integer_col_1: int
    bigint_col_1: int
    varchar_col_1: str
    text_col_1: str
    numeric_col_1: float
    json_col_1: t.Dict[str, t.Any]

    float_col_2: float
    smallint_col_2: int
    integer_col_2: int
    bigint_col_2: int
    varchar_col_2: str
    text_col_2: str
    numeric_col_2: float
    json_col_2: t.Dict[str, t.Any]

    float_col_3: float
    smallint_col_3: int
    integer_col_3: int
    bigint_col_3: int
    varchar_col_3: str
    text_col_3: str
    numeric_col_3: float
    json_col_3: t.Dict[str, t.Any]
