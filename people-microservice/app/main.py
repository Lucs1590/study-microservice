from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.people import people
from app.api.db import database


@asynccontextmanager
async def lifespan(_: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(people, prefix="/api/v1//people", tags=["peolple"])
