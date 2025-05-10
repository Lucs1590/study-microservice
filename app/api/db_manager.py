
from app.api.models import UserInput, UserOutput, UserUpdate
from app.api.db import users, database


async def add_user(payload: UserInput):
    query = users.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_users():
    query = users.select()
    return await database.fetch_all(query=query)


async def get_user(user_id: str):
    query = users.select(users.c.id == user_id)
    return await database.fetch_one(query=query)


async def delete_user(user_id: str):
    query = users.delete().where(users.c.id == user_id)
    return await database.execute(query=query)


async def update_user(user_id: str, payload: UserInput):
    query = (
        users
        .update()
        .where(users.c.id == user_id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
