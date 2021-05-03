from pydantic import BaseModel


class RoasterBase(BaseModel):
    name: str
    url: str


class RoasterCreate(RoasterBase):
    pass


class Roaster(RoasterBase):
    class Config:
        orm_mode = True
