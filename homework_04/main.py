"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from jsonplaceholder_requests import (
    get_post_data,
    get_user_data,
)
from models import (
    AsyncSession,
    async_engine,
    Base,
    Session,
    User,
    Post,
)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(
    session: AsyncSession, name: str, username: str, email: str
) -> User:
    user = User(name=name, username=username, email=email)
    session.add(user)
    print("user create", user)

    await session.commit()
    print("user saved", user)

    return user


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    user: User | None = await session.get(User, user_id)

    print("user", user)
    return user


async def create_post(
    session: AsyncSession,
    user: User,
    title: str,
    body: str,
) -> Post:
    post = Post(title=title, body=body, user=user)
    session.add(post)
    print("post create", post)

    await session.commit()
    print("author saved", post)

    await session.refresh(post)
    print("post refreshed", post)

    return post


async def get_users():
    tasks = set()
    result = []
    for user_id in range(1, 11):
        tasks.add(asyncio.create_task(get_user_data(user_id)))
    done, pending = await asyncio.wait(tasks)
    for elem in done:
        result.append(elem.result())
        t_error = elem.exception()
        if t_error:
            print("Something get wrong:", t_error)
    return sorted(result, key=lambda d: d['id'])


async def get_posts():
    tasks = set()
    result = []
    for post_id in range(1, 101):
        tasks.add(asyncio.create_task(get_post_data(post_id)))
    done, pending = await asyncio.wait(tasks)
    for elem in done:
        result.append(elem.result())
        t_error = elem.exception()
        if t_error:
            print("Something get wrong:", t_error)
    return sorted(result, key=lambda d: d['id'])


async def async_main():
    await create_tables()

    users_dict, post_dict = await asyncio.gather(get_users(), get_posts())

    async with Session() as session:
        for elem in users_dict:
            await create_user(
                session,
                elem.get("name"),
                elem.get("username"),
                elem.get("email"),
            )

        for elem in post_dict:
            post_author = await get_user_by_id(session, elem.get("userId"))
            await create_post(
                session,
                post_author,
                elem.get("title"),
                elem.get("body"),
            )


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
