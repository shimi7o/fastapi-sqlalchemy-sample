from pydantic import BaseModel
from schemas.parent5 import Parent5


class Child5(BaseModel):
    id: int
    name: str
    parents: list[Parent5]

    class Config:
        orm_mode = True
