from pydantic import BaseModel
from schemas.child2 import Child2


class Parent2(BaseModel):
    id: int
    name: str
    child: Child2

    class Config:
        orm_mode = True
