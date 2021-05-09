from sqlalchemy.orm import Session

from app.models.roaster import Roaster
from app.schemas.roaster import RoasterCreate


def get_roasters(db: Session):
    return db.query(Roaster).all()


def create_roaster(db: Session, roaster: RoasterCreate):
    db_roaster = Roaster(
        name=roaster.name,
        url=roaster.url,
        province=roaster.province,
        country=roaster.country,
    )
    db.add(db_roaster)
    db.commit()
    db.refresh(db_roaster)
    return db_roaster
