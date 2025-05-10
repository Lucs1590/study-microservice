from typing import List
from datetime import datetime

from fastapi import APIRouter, APIRouter, HTTPException, Response

from app.api.models import User


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


@users.get("/", response_model=List[User])
async def read_root():
    return users_db


@users.post("/", response_model=User, status_code=201)
async def create_user(user: User):
    user.created_at = datetime.now().isoformat()
    user.updated_at = datetime.now().isoformat()
    users_db.append(user.model_dump())
    return user


@users.put("/{user_id}")
async def update_user(user_id: str, user: User):
    for db_user in users_db:
        if db_user["id"] == user_id:
            db_user.update(user.model_dump(exclude_unset=True))
            db_user["updated_at"] = datetime.now().isoformat()
            return db_user
    raise HTTPException(status_code=404, detail="User not found!")


@users.delete("/{user_id}", status_code=204)
async def delete_user(user_id: str):
    for db_user in users_db[:]:
        if db_user["id"] == user_id:
            users_db.remove(db_user)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="User not found!")
