from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.child2 import Child2  # noqa: F401


class Parent2(Base):
    __tablename__ = "parent2_table"
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey("child2_table.id"))
    child = relationship("Child2", backref="parents")
    name = Column(String(255))
