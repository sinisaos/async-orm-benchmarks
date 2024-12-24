import decimal

from django.db import models


def get_default():
    return {"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}


class CustomJsonField(models.JSONField):
    def from_db_value(self, value, expression, connection):
        if isinstance(value, dict):
            return value
        return super().from_db_value(value, expression, connection)


class BaseUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    superuser = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = "base_user"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "tag"


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        Tag, related_name="tags", through="QuestionTag"
    )

    class Meta:
        managed = False
        db_table = "question"


class QuestionTag(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = "question_tag"


class Answer(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField()
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, related_name="question_answers", on_delete=models.CASCADE
    )

    class Meta:
        managed = False
        db_table = "answer"


class MegaTable(models.Model):
    float_col_1 = models.FloatField(default=2.2)
    smallint_col_1 = models.SmallIntegerField(default=2)
    integer_col_1 = models.PositiveIntegerField(default=2000000)
    bigint_col_1 = models.BigIntegerField(default=99999999)
    varchar_col_1 = models.CharField(max_length=255, default="value1")
    text_col_1 = models.TextField(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_1 = models.DecimalField(
        max_digits=5, decimal_places=2, default=decimal.Decimal("2.2")
    )
    json_col_1 = CustomJsonField(default=get_default)

    float_col_2 = models.FloatField(default=2.2)
    smallint_col_2 = models.SmallIntegerField(default=2)
    integer_col_2 = models.PositiveIntegerField(default=2000000)
    bigint_col_2 = models.BigIntegerField(default=99999999)
    varchar_col_2 = models.CharField(max_length=255, default="value1")
    text_col_2 = models.TextField(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_2 = models.DecimalField(
        max_digits=5, decimal_places=2, default=decimal.Decimal("2.2")
    )
    json_col_2 = CustomJsonField(default=get_default)

    float_col_3 = models.FloatField(default=2.2)
    smallint_col_3 = models.SmallIntegerField(default=2)
    integer_col_3 = models.PositiveIntegerField(default=2000000)
    bigint_col_3 = models.BigIntegerField(default=99999999)
    varchar_col_3 = models.CharField(max_length=255, default="value1")
    text_col_3 = models.TextField(
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old."
    )
    numeric_col_3 = models.DecimalField(
        max_digits=5, decimal_places=2, default=decimal.Decimal("2.2")
    )
    json_col_3 = CustomJsonField(default=get_default)

    class Meta:
        managed = False
        db_table = "mega_table"
