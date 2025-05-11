from uuid import uuid4
from typing import List
from datetime import datetime

from fastapi import APIRouter, HTTPException, Response

from app.api.models import UserInput, UserOutput
from app.api import db_manager

users = APIRouter()


@users.get("/", response_model=List[UserOutput])
async def read_users():
    return await db_manager.get_all_users()


@users.get("/{user_id}", response_model=UserOutput)
async def read_user(user_id: str):
    user = await db_manager.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found!")


@users.post("/", response_model=UserOutput, status_code=201)
async def create_user(payload: UserInput):
    payload = payload.model_dump()
    payload['id'] = str(uuid4())
    payload['created_at'] = datetime.now().isoformat()
    payload['updated_at'] = datetime.now().isoformat()

    validate_user_input(payload)
    if await db_manager.get_user_by_email(payload.get('email')):
        raise HTTPException(status_code=400, detail="Email already exists!")

    user_id = await db_manager.add_user(payload)

    return {'id': user_id}


@users.put("/{user_id}", response_model=UserOutput)
async def update_user(user_id: str, payload: UserInput):
    user = await db_manager.get_user_by_id(user_id)
    if user:
        update_data = payload.model_dump(exclude_unset=True)
        user_db_input = UserInput(**user)
        for key, value in update_data.items():
            setattr(user_db_input, key, value)

        validate_user_input(
            user_db_input.model_dump(),
            fields=['email', 'password']
        )

        payload = user_db_input.model_dump()
        payload['updated_at'] = datetime.now().isoformat()
        payload['created_at'] = user['created_at']
        if payload['email'] != user['email']:
            existing_user = await db_manager.get_user_by_email(payload['email'])
            if existing_user:
                raise HTTPException(
                    status_code=400,
                    detail="Email already exists!"
                )

        db_user = await db_manager.update_user(user_id, payload)
        if db_user:
            return {'id': user_id, **payload}
        raise HTTPException(status_code=400, detail="User not updated!")
    else:
        raise HTTPException(status_code=404, detail="User not found!")


def validate_user_input(user_input_data, fields=['id', 'email', 'password']):
    for field in fields:
        if field not in user_input_data:
            raise HTTPException(
                status_code=400, detail=f"{field.capitalize()} is required!"
            )


@users.delete("/{user_id}", status_code=204)
async def delete_user(user_id: str):
    user = await db_manager.get_user_by_id(user_id)
    if user:
        await db_manager.delete_user(user_id)
        return Response(status_code=204)
    raise HTTPException(status_code=404, detail="User not found!")
