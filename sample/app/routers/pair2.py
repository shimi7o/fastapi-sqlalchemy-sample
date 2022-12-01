from __future__ import annotations
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models.parent2 as models_parent2
import models.child2 as models_child2
import schemas.parent2 as schemas_parent2
import schemas.child5 as schemas_child5

router = APIRouter()


# create
@router.post("/pair2", tags=["多対1"])
def create_pair2(db: Session = Depends(get_db)):
    parent2 = models_parent2.Parent2(
        id=1, child=models_child2.Child2(id=1, name="child2"), name="parent2"
    )
    db.add(parent2)
    db.commit()
    return


# read
@router.get("/pair2-by-parent-id", response_model=schemas_parent2.Parent2, tags=["多対1"])
def get_pair2_by_parent_id(db: Session = Depends(get_db)):
    parent = (
        db.query(models_parent2.Parent2)
        # Child2を指定しないほうがpydanticの型に直接変換できて簡単
        # db.query(models_parent2.Parent2, models_child2.Child2)
        .filter(models_parent2.Parent2.id == 1).one()
    )
    return parent


@router.get(
    "/pair2-by-child-id", response_model=schemas_child5.Child5, tags=["多対1"]
)
def get_pair2_by_child_id(db: Session = Depends(get_db)):
    child = db.query(models_child2.Child2).filter(models_child2.Child2.id == 1).one()
    return child
