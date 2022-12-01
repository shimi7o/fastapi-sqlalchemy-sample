from pydantic import BaseModel
from schemas.child1 import Child1


class Parent1(BaseModel):
    id: int
    name: str
    children: list[Child1]

    class Config:
        orm_mode = True
