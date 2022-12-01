from pydantic import BaseModel
from schemas.parent6 import Parent6


class Child6(BaseModel):
    id: int
    name: str
    parents: list[Parent6]

    class Config:
        orm_mode = True
