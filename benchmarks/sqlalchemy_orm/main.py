from fastapi import Depends, FastAPI
from fastapi.responses import ORJSONResponse
from models import Answer, MegaTable, Question, Tag
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import selectinload

engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@localhost:5432/perfdb",
    pool_size=10,
)

async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with async_session() as session:
        yield session


app = FastAPI(default_response_class=ORJSONResponse)


@app.get("/small-table/")
async def tags_list(session=Depends(get_session)):
    data = (await session.execute(select(Tag).limit(50))).scalars()
    return data.all()


@app.get("/small-table/{pk:int}/")
async def tag_single(pk: int, session=Depends(get_session)):
    data = (await session.execute(select(Tag).where(Tag.id == pk))).scalar()
    return data


@app.get("/related-table/")
async def questions_list(session=Depends(get_session)):
    data = (
        await session.execute(
            select(Question)
            .limit(50)
            .options(
                selectinload(Question.question_user),
                selectinload(Question.tags),
            )
        )
    ).scalars()
    return data.all()


@app.get("/related-table/{pk:int}/")
async def question_single(
    pk: int, session=Depends(get_session)
) -> ORJSONResponse:
    data = (
        await session.execute(
            select(Question)
            .where(Question.id == pk)
            .options(
                selectinload(Question.question_user),
                selectinload(Question.tags),
            )
        )
    ).scalar()
    data.__dict__["question_answers"] = (
        (await session.execute(select(Answer).where(Answer.question_id == pk)))
        .scalars()
        .all()
    )
    return data


@app.get("/mega-table/")
async def mega_table_list(session=Depends(get_session)):
    data = (await session.execute(select(MegaTable).limit(50))).scalars()
    return data.all()


@app.get("/mega-table/{pk:int}/")
async def mega_table_single(pk: int, session=Depends(get_session)):
    data = (
        (await session.execute(select(MegaTable).where(MegaTable.id == pk)))
        .scalars()
        .all()
    )
    return data
