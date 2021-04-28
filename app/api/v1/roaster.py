from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependacies import get_db
from app.services.roaster import get_roasters, create_roaster
from app.schemas.roaster import Roaster, RoasterCreate

router = APIRouter()


@router.get("/", response_model=List[Roaster])
def read_roasters(db: Session = Depends(get_db)):
    return get_roasters(db)


@router.post("/", response_model=Roaster)
def create_user(roaster: RoasterCreate, db: Session = Depends(get_db)):
    return create_roaster(db=db, roaster=roaster)
