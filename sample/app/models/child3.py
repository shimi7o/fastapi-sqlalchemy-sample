from sqlalchemy import Column, Integer, String
from database import Base


class Child3(Base):
    __tablename__ = "right_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
