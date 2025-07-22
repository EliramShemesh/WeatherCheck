from fastapi import FastAPI, HTTPException
from services import WeatherService

app = FastAPI()
weather_service = WeatherService()

@app.get("/weather")
def get_weather(city: str):
    try:
        return weather_service.get_weather(city)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))