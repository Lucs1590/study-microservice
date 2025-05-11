from app.api.models import PeopleInput
from app.api.db import people, database


async def get_all_people():
    query = people.select()
    return await database.fetch_all(query=query)


async def get_person_by_id(people_id: str):
    query = people.select().where(people.c.id == people_id)
    return await database.fetch_one(query=query)


async def add_people(payload: PeopleInput):
    query = people.insert().values(**payload)

    try:
        await database.execute(query=query)
    except Exception as e:
        raise RuntimeError(f"Error inserting people: {e}") from e
    return payload['id']
