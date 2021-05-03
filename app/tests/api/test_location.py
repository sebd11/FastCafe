from app.tests.test_client import client


def test_read_roasters():
    response = client.get("/api/v1/locations/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
