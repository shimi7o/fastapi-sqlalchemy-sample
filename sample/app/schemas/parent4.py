from pydantic import BaseModel


class Parent4(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
