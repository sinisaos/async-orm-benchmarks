from datetime import datetime
from decimal import Decimal
from typing import Any, List

from sqlalchemy import (
    JSON,
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    SmallInteger,
    String,
    Table,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

Base: Any = declarative_base()

question_tag = Table(
    "question_tag",
    Base.metadata,
    Column("question_id", ForeignKey("question.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)


class BaseUser(Base):
    __tablename__ = "base_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    superuser: Mapped[bool] = mapped_column(Boolean, default=False)


class Question(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now
    )

    views: Mapped[int] = mapped_column(Integer())
    likes: Mapped[int] = mapped_column(Integer())
    user_id: Mapped[int] = mapped_column(ForeignKey("base_user.id"))
    tags: Mapped[List["Tag"]] = relationship(secondary=question_tag)

    question_user: Mapped[BaseUser] = relationship("BaseUser")


class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))


class Answer(Base):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now
    )
    likes: Mapped[int] = mapped_column(Integer())
    user_id: Mapped[int] = mapped_column(ForeignKey("base_user.id"))
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))


class MegaTable(Base):
    __tablename__ = "mega_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    float_col_1: Mapped[float] = mapped_column(Float, default=2.2)
    smallint_col_1: Mapped[int] = mapped_column(SmallInteger, default=2)

    integer_col_1: Mapped[int] = mapped_column(Integer, default=2000000)

    bigint_col_1: Mapped[int] = mapped_column(BigInteger, default=99999999)
    varchar_col_1: Mapped[str] = mapped_column(String(255), default="value1")
    text_col_1: Mapped[str] = mapped_column(
        Text,
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old.",
    )
    numeric_col_1: Mapped[float] = mapped_column(
        Numeric(5, 2), default=Decimal("2.2")
    )
    json_col_1: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True},
    )

    float_col_2: Mapped[float] = mapped_column(Float, default=2.2)
    smallint_col_2: Mapped[int] = mapped_column(SmallInteger, default=2)
    integer_col_2: Mapped[int] = mapped_column(Integer, default=2000000)
    bigint_col_2: Mapped[int] = mapped_column(BigInteger, default=99999999)
    varchar_col_2: Mapped[str] = mapped_column(String(255), default="value1")
    text_col_2: Mapped[str] = mapped_column(
        Text,
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old.",
    )
    numeric_col_2: Mapped[float] = mapped_column(
        Numeric(5, 2), default=Decimal("2.2")
    )
    json_col_2: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True},
    )

    float_col_3: Mapped[float] = mapped_column(Float, default=2.2)
    smallint_col_3: Mapped[int] = mapped_column(SmallInteger, default=2)
    integer_col_3: Mapped[int] = mapped_column(Integer, default=2000000)
    bigint_col_3: Mapped[int] = mapped_column(BigInteger, default=99999999)
    varchar_col_3: Mapped[str] = mapped_column(String(255), default="value1")
    text_col_3: Mapped[str] = mapped_column(
        Text,
        default="Contrary to popular belief, Lorem Ipsum is not simply "
        "random text. It has roots in a piece of classical Latin "
        "literature from 45 BC, making it over 2000 years old.",
    )
    numeric_col_3: Mapped[float] = mapped_column(
        Numeric(5, 2), default=Decimal("2.2")
    )
    json_col_3: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True},
    )
