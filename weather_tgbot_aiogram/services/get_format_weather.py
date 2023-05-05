from datetime import datetime

import pytz
from icon import PICTURES_TIME_OF_DAY
from services.get_weather_n_days import get_weather_n_days
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


def format_weather_n_days(city: str, count: int) -> str:
    """format weather data in string"""

    weather_list = get_weather_n_days(city, count)
    message = f"Погода в городе: <u>{city}</u>:\n"

    for weather in weather_list:
        #  Определение локальных переменных
        date = weather.date.split(" ")[0]
        time = weather.date.split(" ")[1]
        time_h_m = ":".join((time.split(":"))[:2])
        icon_time_of_day = PICTURES_TIME_OF_DAY[time_h_m]

        # Проверка, начался ли новыый день, если да то отображается дата
        if time_h_m == "00:00" or time_h_m == "03:00":
            message += f"****<u>{date}</u>**** \n"

        # Добавление основного текста
        message += (
            f"{icon_time_of_day} \n"
            f"Температура: <b>{weather.temperature}</b>C° "
            f"{weather.weather_description.value}\n"
            f"Скорость ветра: {weather.wind} m/c\n\n"
        )
    return message
