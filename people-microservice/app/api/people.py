from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.api.models import PeopleInput, PeopleOutput
from app.api import db_manager

people = APIRouter()


@people.get("/")
async def get_all_people():
    people_response = await db_manager.get_all_people()
    return people_response


@people.get("/{people_id}", response_model=PeopleOutput, status_code=200)
async def get_people_by_id(people_id: int):
    if people_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="People ID must be a positive integer"
        )
    person_data = await db_manager.get_person_by_id(people_id)
    if not person_data:
        raise HTTPException(status_code=404, detail="People not found")
    return person_data


@people.post("/", response_model=PeopleOutput, status_code=201)
async def create_people(people_input: PeopleInput):
    payload = {
        "name": people_input.name,
        "user_id": people_input.user_id,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    try:
        response = await db_manager.add_people(payload)
    except HTTPException as err:
        raise HTTPException(
            status_code=err.status_code,
            detail=err.detail
        ) from err
    except Exception as err:
        raise HTTPException(
            status_code=500,
            detail=f"Error creating people: {err}"
        ) from err
    return {"id": response, "name": people_input.name}
