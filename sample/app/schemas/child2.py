from pydantic import BaseModel


class Child2(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
