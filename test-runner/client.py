import requests

class WeatherApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_weather(self, city: str):
        return requests.get(f"{self.base_url}/weather", params={"city": city})