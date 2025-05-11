from pydantic import BaseModel


class UserInput(BaseModel):
    email: str
    password: str


class UserOutput(BaseModel):
    id: str


class UserUpdate(BaseModel):
    email: str | None = None
    password: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
