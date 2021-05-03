from typing import List
from pydantic import BaseModel


class ProvinceBase(BaseModel):
    name: str


class Province(ProvinceBase):
    class Config:
        orm_mode = True


class CountryBase(BaseModel):
    name: str
    has_states: bool


class Country(CountryBase):
    provinces: List[Province] = []

    class Config:
        orm_mode = True
