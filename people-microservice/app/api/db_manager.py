from fastapi import HTTPException
from app.api.models import PeopleInput
from app.api.db import people, database
from app.api.service import get_user


async def get_all_people():
    query = people.select()
    return await database.fetch_all(query=query)


async def get_person_by_id(people_id: str):
    query = people.select().where(people.c.id == people_id)
    return await database.fetch_one(query=query)


async def add_people(payload: PeopleInput):
    user = await get_user(payload.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    query = people.insert().values(**payload)

    try:
        response = await database.execute(query=query)
    except Exception as e:
        raise RuntimeError(f"Error inserting people: {e}") from e
    return response
