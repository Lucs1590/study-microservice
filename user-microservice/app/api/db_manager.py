
from app.api.models import UserInput, UserOutput, UserUpdate
from app.api.db import users, database


async def add_user(payload: dict):
    query = users.insert().values(**payload)

    try:
        await database.execute(query=query)
    except Exception as e:
        raise RuntimeError(f"Error inserting user: {e}") from e
    return payload['id']


async def get_all_users():
    query = users.select()
    return await database.fetch_all(query=query)


async def get_user_by_id(user_id: str):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query=query)


async def get_user_by_email(email: str):
    query = users.select().where(users.c.email == email)
    return await database.fetch_one(query=query)


async def delete_user(user_id: str):
    query = users.delete().where(users.c.id == user_id)
    return await database.execute(query=query)


async def update_user(user_id: str, payload: UserInput):
    query = (
        users
        .update()
        .where(users.c.id == user_id)
        .values(**payload)
        .returning(users.c.id, users.c.email, users.c.created_at, users.c.updated_at)
    )
    return await database.execute(query=query)
