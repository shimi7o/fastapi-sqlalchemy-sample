from pydantic import BaseModel


class Parent6(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
