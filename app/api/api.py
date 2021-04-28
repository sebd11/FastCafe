from fastapi import APIRouter

from app.api.v1 import roaster

router = APIRouter(prefix="/v1")
router.include_router(roaster.router, prefix="/roasters", tags=["roasters"])
