import decimal

from tortoise import fields
from tortoise.models import Model


class BaseUser(Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    superuser = fields.BooleanField(default=False)

    class Meta:
        table = "base_user"


class Question(Model):
    id = fields.IntField(primary_key=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)
    views = fields.IntField()
    likes = fields.IntField()
    user: fields.ForeignKeyRelation[BaseUser] = fields.ForeignKeyField(
        "models.BaseUser",
        related_name="question_user",
        on_delete=fields.CASCADE,
    )
    tags = fields.ManyToManyField(
        "models.Tag",
        related_name="tags",
        through="question_tag",
    )

    class Meta:
        table = "question"


class Tag(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)

    class Meta:
        table = "tag"


class Answer(Model):
    id = fields.IntField(primary_key=True)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)
    likes = fields.IntField()
    user: fields.ForeignKeyRelation[BaseUser] = fields.ForeignKeyField(
        "models.BaseUser",
        related_name="answer_user",
        on_delete=fields.CASCADE,
    )
    question: fields.ForeignKeyRelation[Question] = fields.ForeignKeyField(
        "models.Question",
        related_name="answers_question",
        on_delete=fields.CASCADE,
    )

    class Meta:
        table = "answer"


class MegaTable(Model):
    float_col_1 = fields.FloatField(default=2.2)
    smallint_col_1 = fields.SmallIntField(default=2)
    integer_col_1 = fields.IntField(default=2000000)
    bigint_col_1 = fields.BigIntField(default=99999999)
    varchar_col_1 = fields.CharField(max_length=255, default="value1")
    text_col_1 = fields.TextField(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_1 = fields.DecimalField(5, 2, default=decimal.Decimal("2.2"))
    json_col_1: fields.JSONField = fields.JSONField(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}
    )

    float_col_2 = fields.FloatField(default=2.2)
    smallint_col_2 = fields.SmallIntField(default=2)
    integer_col_2 = fields.IntField(default=2000000)
    bigint_col_2 = fields.BigIntField(default=99999999)
    varchar_col_2 = fields.CharField(max_length=255, default="value1")
    text_col_2 = fields.TextField(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_2 = fields.DecimalField(5, 2, default=decimal.Decimal("2.2"))
    json_col_2: fields.JSONField = fields.JSONField(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}
    )

    float_col_3 = fields.FloatField(default=2.2)
    smallint_col_3 = fields.SmallIntField(default=2)
    integer_col_3 = fields.IntField(default=2000000)
    bigint_col_3 = fields.BigIntField(default=99999999)
    varchar_col_3 = fields.CharField(max_length=255, default="value1")
    text_col_3 = fields.TextField(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_3 = fields.DecimalField(5, 2, default=decimal.Decimal("2.2"))
    json_col_3: fields.JSONField = fields.JSONField(
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}
    )

    class Meta:
        table = "mega_table"
