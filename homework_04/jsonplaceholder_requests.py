"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_user_data(user_id: int):

    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL + "/" + str(user_id)) as response:

            return await response.json()


async def get_post_data(post_id: int):

    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL + "/" + str(post_id)) as response:

            return await response.json()


async def get_users():
    tasks = set()
    result = []
    for user_id in range(1, 11):
        tasks.add(asyncio.create_task(get_user_data(user_id)))
    done, pending = await asyncio.wait(tasks)
    for el in done:
        result.append(el.result())
        t_error = el.exception()
        if t_error:
            print("Something get wrong:", t_error)
    return sorted(result, key=lambda d: d['id'])


async def get_posts():
    tasks = set()
    result = []
    for post_id in range(1, 101):
        tasks.add(asyncio.create_task(get_post_data(post_id)))
    done, pending = await asyncio.wait(tasks)
    for el in done:
        result.append(el.result())
        t_error = el.exception()
        if t_error:
            print("Something get wrong:", t_error)
    return sorted(result, key=lambda d: d['id'])


async def main():
    user_data, post_data = await asyncio.gather(get_users(), get_posts())
    for elem in user_data:
        print("User_data", elem)
    for elem in post_data:
        print("Post_data", elem)


if __name__ == "__main__":
    asyncio.run(main())
