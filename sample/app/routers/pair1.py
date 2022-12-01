from __future__ import annotations
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models.parent1 as models_parent1
import models.child1 as models_child1
import schemas.parent1 as schemas_parent1
import schemas.child4 as schemas_child4

router = APIRouter()


# create
@router.post("/pair1", tags=["1対多"])
def create_pair1(db: Session = Depends(get_db)):
    parent = models_parent1.Parent1(
        id=1, children=[models_child1.Child1(id=1, name="child1")], name="parent1"
    )
    db.add(parent)
    db.commit()
    return


# read
@router.get("/pair1-by-parent-id", response_model=schemas_parent1.Parent1, tags=["1対多"])
def get_pair1_by_parent_id(db: Session = Depends(get_db)):
    parent = (
        db.query(models_parent1.Parent1)
        # db.query(models_parent1.Parent1, models_child1.Child1)
        # Child1を指定しないと戻り値の型は<class 'models.parent1.Parent1>
        # Child1を指定しないと戻り値の型は<class 'sqlalchemy.engine.row.Row'>
        # Child1を指定しないほうがpydanticの型に直接変換できて簡単
        # Child1を指定しない場合はjoinは無意味なので指定しない
        # .join(models_child1.Child1, models_parent1.Parent1.children)
        .filter(models_parent1.Parent1.id == 1).one()
    )
    return parent


@router.get("/pair1-by-child-id", response_model=schemas_child4.Child4, tags=["1対多"])
def get_pair1_by_child_id(db: Session = Depends(get_db)):
    child = db.query(models_child1.Child1).filter(models_child1.Child1.id == 1).one()
    return child
