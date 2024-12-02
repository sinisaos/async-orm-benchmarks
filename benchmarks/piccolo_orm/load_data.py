import asyncio
import random

from tables import (
    Answer,
    BaseUser,
    MegaTable,
    Question,
    QuestionTag,
    Tag,
)


async def main():
    # Tables creating
    await BaseUser.create_table(if_not_exists=True)
    await Question.create_table(if_not_exists=True)
    await Tag.create_table(if_not_exists=True)
    await QuestionTag.create_table(if_not_exists=True)
    await Answer.create_table(if_not_exists=True)
    await MegaTable.create_table(if_not_exists=True)

    data = BaseUser(
        username="piccolo",
        email="piccolo@example.com",
        superuser=True,
    )
    await data.save()

    for item in range(1, 101):
        data = Question(
            title=f"Question {item}",
            content=f"Question {item}",
            views=10,
            likes=10,
            user_id=1,
        )
        await data.save()

    for item in range(1, 101):
        data = Tag(
            name=f"Tag {item}",
        )
        await data.save()

    for _ in range(1, 101):
        data = QuestionTag(
            question_id=random.randint(1, 25),
            tag_id=random.randint(1, 25),
        )
        await data.save()

    for item in range(1, 101):
        data = Answer(
            content=f"Answer {item}",
            likes=20,
            user_id=1,
            question_id=random.randint(1, 50),
        )
        await data.save()

    for _ in range(1, 101):
        data = MegaTable()
        await data.save()

    print("Finished!")


if __name__ == "__main__":
    asyncio.run(main())
