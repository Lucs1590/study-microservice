from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(default=str(uuid4()))
    email: str
    password: str
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())
