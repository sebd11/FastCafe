import logging

from sqlalchemy.orm import Session

from app.models.location import Country, Province

logger = logging.getLogger(__name__)


provinces = [
    "Quebec",
    "Ontario",
    "Manitoba",
    "Saskatchewan",
    "Alberta",
    "British Columbia",
    "New Brunswick",
    "Nova Scotia",
    "Prince Edward Island",
    "Newfoundland and Labrador",
    "Nunavut",
    "Yukon",
    "Northwest Territories",
]


def init_locations(db: Session):
    if db.query(Country).filter(Country.name == "Canada").first() is None:
        logger.info("Initializing countries...")
        db_country = Country(name="Canada", has_states=False)
        db.add(db_country)
        db_provinces = []
        for province in provinces:
            db_provinces.append(Province(name=province, country=db_country))
        db.add_all(db_provinces)
        db.commit()
