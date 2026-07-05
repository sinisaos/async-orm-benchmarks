from datetime import datetime
from decimal import Decimal

from oxyde import Field, Model


class BaseUser(Model):
    id: int | None = Field(default=None, db_pk=True)
    username: str
    email: str
    superuser: bool = Field(default=False)

    class Meta:
        is_table = True
        table_name = "base_user"


class Question(Model):
    id: int | None = Field(default=None, db_pk=True)
    title: str
    content: str = Field(db_type="TEXT")
    created_at: datetime = Field(db_default="CURRENT_TIMESTAMP")
    updated_at: datetime | None = Field(default=None)
    views: int
    likes: int
    user: BaseUser | None = Field(default=None, db_on_delete="CASCADE")
    tags: list["Tag"] = Field(db_m2m=True, db_through="QuestionTag")
    answers: list["Answer"] = Field(db_reverse_fk="question")

    class Meta:
        is_table = True
        table_name = "question"


class Tag(Model):
    id: int | None = Field(default=None, db_pk=True)
    name: str

    class Meta:
        is_table = True
        table_name = "tag"


class QuestionTag(Model):
    id: int | None = Field(default=None, db_pk=True)
    question: Question | None = Field(default=None, db_on_delete="CASCADE")
    tag: Tag | None = Field(default=None, db_on_delete="CASCADE")

    class Meta:
        is_table = True
        table_name = "question_tag"


class Answer(Model):
    id: int | None = Field(default=None, db_pk=True)
    content: str = Field(db_type="TEXT")
    created_at: datetime = Field(db_default="CURRENT_TIMESTAMP")
    updated_at: datetime | None = Field(default=None)
    likes: int
    user: BaseUser | None = Field(default=None, db_on_delete="CASCADE")
    question: Question | None = Field(default=None, db_on_delete="CASCADE")

    class Meta:
        is_table = True
        table_name = "answer"


class MegaTable(Model):
    id: int | None = Field(default=None, db_pk=True)
    float_col_1: float = Field(default=2.2)
    smallint_col_1: int | None = Field(default=2, db_type="SMALLINT")
    integer_col_1: int = Field(default=2000000)
    bigint_col_1: int = Field(default=99999999)
    varchar_col_1: str = Field(default="value1")
    text_col_1: str = Field(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old.",
        db_type="TEXT",
    )
    numeric_col_1: Decimal | None = Field(
        max_digits=5, decimal_places=2, default=Decimal("2.2")
    )
    json_col_1: dict = Field(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True},
        db_type="JSON",
    )

    float_col_2: float = Field(default=2.2)
    smallint_col_2: int | None = Field(default=2, db_type="SMALLINT")
    integer_col_2: int = Field(default=2000000)
    bigint_col_2: int = Field(default=99999999)
    varchar_col_2: str = Field(default="value1")
    text_col_2: str = Field(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old.",
        db_type="TEXT",
    )
    numeric_col_2: Decimal | None = Field(
        max_digits=5, decimal_places=2, default=Decimal("2.2")
    )
    json_col_2: dict = Field(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True},
        db_type="JSON",
    )

    float_col_3: float = Field(default=2.2)
    smallint_col_3: int | None = Field(default=2, db_type="SMALLINT")
    integer_col_3: int = Field(default=2000000)
    bigint_col_3: int = Field(default=99999999)
    varchar_col_3: str = Field(default="value1")
    text_col_3: str = Field(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old.",
        db_type="TEXT",
    )
    numeric_col_3: Decimal | None = Field(
        max_digits=5, decimal_places=2, default=Decimal("2.2")
    )
    json_col_3: dict = Field(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True},
        db_type="JSON",
    )

    class Meta:
        is_table = True
        table_name = "mega_table"
