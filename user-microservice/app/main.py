from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.users import users
from app.api.db import database, create_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    await database.connect()
    await create_database()
    yield
    await database.disconnect()

app = FastAPI(
    lifespan=lifespan,
    openapi_url="/api/v1/users/openapi.json",
    docs_url="/api/v1/users/docs",
    redoc_url="/api/v1/users/redoc"
)

app.include_router(users, prefix="/api/v1/users", tags=["users"])
