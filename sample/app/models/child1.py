from sqlalchemy import Column, Integer, ForeignKey, String
from database import Base


class Child1(Base):
    __tablename__ = "child1_table"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent1_table.id"))
    name = Column(String(255))
