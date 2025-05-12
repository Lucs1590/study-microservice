from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.people import people
from app.api.db import database, create_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    await database.connect()
    await create_database()
    yield
    await database.disconnect()

app = FastAPI(
    lifespan=lifespan,
    openapi_url="/api/v1/people/openapi.json",
    docs_url="/api/v1/people/docs",
    redoc_url="/api/v1/people/redoc"
)

app.include_router(people, prefix="/api/v1/people", tags=["people"])
