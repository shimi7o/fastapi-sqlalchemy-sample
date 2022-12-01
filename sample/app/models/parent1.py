from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.child1 import Child1  # noqa: F401


class Parent1(Base):
    __tablename__ = "parent1_table"
    id = Column(Integer, primary_key=True)
    children = relationship("Child1", backref="parent")
    name = Column(String(255))
