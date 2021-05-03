from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependacies import get_db
from app.services.location import get_countries
from app.schemas.location import Country

router = APIRouter()


@router.get("/", response_model=List[Country])
def read_countries(db: Session = Depends(get_db)):
    return get_countries(db)
