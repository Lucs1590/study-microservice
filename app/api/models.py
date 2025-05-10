from uuid import uuid4
from datetime import datetime
from typing import List, Dict, Any
from pydantic import BaseModel, Field


class Report(BaseModel):
    id: str = Field(default=str(uuid4()))
    content: Dict[str, Any]
    status: str = Field(default="pending")
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    user_id: int
