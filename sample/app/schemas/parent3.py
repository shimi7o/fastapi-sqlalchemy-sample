from pydantic import BaseModel
from schemas.child3 import Child3


class Parent3(BaseModel):
    id: int
    name: str
    children: list[Child3]

    class Config:
        orm_mode = True
