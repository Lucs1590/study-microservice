from pydantic import BaseModel


class PeopleInput(BaseModel):
    name: str
    user_id: str

class PeopleOutput(BaseModel):
    id: int
    name: str