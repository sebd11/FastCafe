from fastapi import FastAPI, Depends

from app.api import api
from app.db.database import Base, engine, SessionLocal
from app.tests.init_db import init_locations


Base.metadata.create_all(bind=engine)
db = SessionLocal()
init_locations(db)
db.close()


app = FastAPI(title="FastCafe", port=8000)

app.include_router(api.router, prefix="/api")
