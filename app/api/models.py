from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class UserInput(BaseModel):
    id: str = Field(default=str(uuid4()))
    email: str
    password: str
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())


class UserOutput(BaseModel):
    id: str


class UserUpdate(BaseModel):
    email: str | None = None
    password: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
