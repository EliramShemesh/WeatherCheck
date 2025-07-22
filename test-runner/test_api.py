import pytest
from client import WeatherApiClient

@pytest.fixture(scope="module")
def client():
    return WeatherApiClient("http://weather-api.default.svc.cluster.local:8000")

def test_london_weather(client):
    response = client.get_weather("London")
    assert response.status_code == 200
    data = response.json()
    assert data["temperature"] == 18
    assert data["unit"] == "C"

def test_invalid_city(client):
    response = client.get_weather("Atlantis")
    assert response.status_code == 404