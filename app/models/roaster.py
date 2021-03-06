from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Roaster(Base):
    __tablename__ = "roasters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String, index=True, unique=True)
    province = Column(String)
    country = Column(String)
