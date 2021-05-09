from fastapi import FastAPI

from app.api import api
from app.db.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastCafe", port=8000)

app.include_router(api.router, prefix="/api")
