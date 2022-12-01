from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.child3 import Child3  # noqa: F401
from models.association import association_table  # noqa: F401


class Parent3(Base):
    __tablename__ = "left_table"
    id = Column(Integer, primary_key=True)
    children = relationship("Child3", secondary=association_table, backref="parents")
    name = Column(String(255))
