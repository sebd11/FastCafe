from app.tests.test_client import client


def test_create_roaster():
    test_roaster = {
        "name": "test_roaster1",
        "url": "https://roaster1.com",
        "province": "quebec",
        "country": "canada",
    }

    response = client.post(
        "/api/v1/roasters/",
        json=test_roaster,
    )
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == test_roaster["name"]
    assert data["url"] == test_roaster["url"]
    assert data["province"] == test_roaster["province"]
    assert data["country"] == test_roaster["country"]


def test_read_roasters():
    response = client.get("/api/v1/roasters/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
