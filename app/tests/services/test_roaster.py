from app.tests.test_client import client


def test_create_roaster():
    test_roaster = {
        "name": "test_roaster1",
        "url": "https://roaster1.com",
    }
    response = client.post(
        "/api/v1/roasters/",
        json=test_roaster,
    )
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == test_roaster["name"]
    assert data["url"] == test_roaster["url"]


def test_read_roasters():
    response = client.get("/api/v1/roasters/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
