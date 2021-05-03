from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    has_states = Column(Boolean, default=False)
    provinces = relationship("Province", back_populates="country")


class Province(Base):
    __tablename__ = "provinces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))
    country = relationship("Country", back_populates="provinces")
