from sqlalchemy.orm import Session

from app.models.roaster import RoasterModel
from app.schemas.roaster import RoasterCreate


def get_roasters(db: Session):
    return db.query(RoasterModel).all()


def create_roaster(db: Session, roaster: RoasterCreate):
    db_roaster = RoasterModel(name=roaster.name)
    db.add(db_roaster)
    db.commit()
    db.refresh(db_roaster)
    return db_roaster
