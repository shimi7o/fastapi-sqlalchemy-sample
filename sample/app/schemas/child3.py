from pydantic import BaseModel


class Child3(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
