from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.users import users
from app.api.db import database


@asynccontextmanager
async def lifespan(_: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(users, prefix="/users", tags=["Users"])
