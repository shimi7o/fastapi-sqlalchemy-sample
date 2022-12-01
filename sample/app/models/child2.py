from sqlalchemy import Column, Integer, String
from database import Base


class Child2(Base):
    __tablename__ = "child2_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
