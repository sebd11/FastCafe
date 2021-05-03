from sqlalchemy.orm import Session

from app.models.location import Country, Province


def get_countries(db: Session):
    return db.query(Country).all()
