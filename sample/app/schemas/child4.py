from pydantic import BaseModel
from schemas.parent4 import Parent4


class Child4(BaseModel):
    id: int
    name: str
    parent: Parent4

    class Config:
        orm_mode = True
