class WeatherService:
    def get_weather(self, city: str) -> dict:
        data = {
            "london": {"temperature": 18, "unit": "C"},
            "paris": {"temperature": 22, "unit": "C"}
        }
        city_lower = city.lower()
        if city_lower in data:
            return {"city": city, **data[city_lower]}
        raise ValueError("City not found")