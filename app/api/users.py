from typing import List
from datetime import datetime

from fastapi import APIRouter, HTTPException, Response

from app.api.models import UserInput, UserOutput
from app.api import db_manager


users_db = [
    {
        "id": "fc43c30d-61d3-4739-a53d-9ea679c23c91",
        "email": "example@example.com",
        "password": "1234",
        "created_at": "2025-05-10T19:14:03.606753",
        "updated_at": "2025-05-10T19:14:03.606782",
    }
]

users = APIRouter()


@users.get("/", response_model=List[UserOutput])
async def read_root():
    return await db_manager.get_all_users()


@users.post("/", status_code=201)
async def create_user(payload: UserInput):
    payload.created_at = datetime.now().isoformat()
    payload.updated_at = datetime.now().isoformat()
    user_id = await db_manager.add_user(payload)
    response = {'id': user_id, **payload.model_dump()}
    return response


@users.put("/{user_id}")
async def update_user(user_id: str, payload: UserInput):
    user = await db_manager.get_user(user_id)
    if user:
        update_data = payload.model_dump(exclude_unset=True)
        user_db_input = UserInput(**user)
        user_db_input.model_update(update_data)

        payload = user_db_input.model_dump()
        payload.updated_at = datetime.now().isoformat()
        payload.created_at = user["created_at"]
        db_user = await db_manager.update_user(user_id, payload)
        if db_user:
            return {'id': user_id, **payload.model_dump()}
    else:
        raise HTTPException(status_code=404, detail="User not found!")


@users.delete("/{user_id}", status_code=204)
async def delete_user(user_id: str):
    user = await db_manager.get_user(user_id)
    if user:
        await db_manager.delete_user(user_id)
        return Response(status_code=204)
    raise HTTPException(status_code=404, detail="User not found!")
