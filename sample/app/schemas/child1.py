from pydantic import BaseModel


class Child1(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
