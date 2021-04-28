from fastapi import FastAPI, Depends

from app.api import api

from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


app = FastAPI(title="FastCafe")

app.include_router(api.router, prefix="/api")
