from __future__ import annotations
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models.parent3 as models_parent3
import models.child3 as models_child3
import schemas.parent3 as schemas_parent3
import schemas.child6 as schemas_child6

router = APIRouter()


# create
@router.post("/pair3", tags=["多対多"])
def create_pair3(db: Session = Depends(get_db)):
    # 中間テーブルにも値が入る
    parent = models_parent3.Parent3(
        id=1, children=[models_child3.Child3(id=1, name="child3")], name="parent3"
    )
    db.add(parent)
    db.commit()
    return


# read
@router.get("/pair3-by-parent-id", response_model=schemas_parent3.Parent3, tags=["多対多"])
def get_pair3_by_parent_id(db: Session = Depends(get_db)):
    parent = (
        db.query(models_parent3.Parent3).filter(models_parent3.Parent3.id == 1).one()
    )
    return parent


@router.get("/pair3-by-child-id", response_model=schemas_child6.Child6, tags=["多対多"])
def get_pair3_by_child_id(db: Session = Depends(get_db)):
    child = db.query(models_child3.Child3).filter(models_child3.Child3.id == 1).one()
    return child
