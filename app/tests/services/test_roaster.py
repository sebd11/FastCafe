from app.tests.test_client import client


def test_create_roaster():
    response = client.post(
        "/api/v1/roasters/",
        json={"name": "test_roaster1"},
    )
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "test_roaster1"


def test_read_roasters():
    response = client.get("/api/v1/roasters/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
