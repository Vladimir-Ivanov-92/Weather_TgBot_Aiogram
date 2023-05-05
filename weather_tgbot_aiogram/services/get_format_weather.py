from datetime import datetime

import pytz
from services.get_weather_now import get_weather_now_new


def format_weather_now(city: str) -> str:
    """format weather data in string"""
    weather = get_weather_now_new(city)
    tz_moscow = pytz.timezone('Europe/Moscow')
    return (
        f"***{datetime.now(tz_moscow).strftime('%Y-%m-%d  %H:%M')}***\n"
        f"Погода в городе {city}:\nТемпература: {weather.temperature} C°"
        f"{weather.weather_description.value}\n"
        f"Скорость ветра: {weather.wind} m/c\n"
        f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
        f"Закат: {weather.sunset.strftime('%H:%M')}\n"
        f"***Хорошего дня!***"
    )
