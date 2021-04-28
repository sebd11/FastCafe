from pydantic import BaseModel


class RoasterBase(BaseModel):
    name: str


class RoasterCreate(RoasterBase):
    pass


class Roaster(RoasterBase):
    class Config:
        orm_mode = True
