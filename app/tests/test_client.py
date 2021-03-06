from fastapi.testclient import TestClient

from app.main import app
from app.dependacies import get_db
from app.db.database import Base, test_engine, TestingSessionLocal


Base.metadata.drop_all(bind=test_engine)
Base.metadata.create_all(bind=test_engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
