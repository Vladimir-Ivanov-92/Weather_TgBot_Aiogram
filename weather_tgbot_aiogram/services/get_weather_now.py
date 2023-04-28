from datetime import datetime

import pytz
import requests
from config import config
from icon import code_to_smile
from models.pydantic_models import WeatherNowJson


def get_weather_now(city):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}"
                         f"&appid={config.open_weather_token.get_secret_value()}"
                         "&units=metric&lang=ru"
                         )
        data = WeatherNowJson.parse_raw(r.content)
        city = data.name
        cur_weather = data.main["temp"]
        wind = data.wind["speed"]
        weather_description = data.weather[0].main

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            message_reply = ("Посмотри в окно! Не пойму что там происходит!")

        tz_moscow = pytz.timezone('Europe/Moscow')
        sunrise = datetime.fromtimestamp(data.sys["sunrise"])
        sunset = datetime.fromtimestamp(data.sys["sunset"])
        message_reply = (
            f"***{datetime.now(tz_moscow).strftime('%Y-%m-%d  %H:%M')}***\n"
            f"Погода в городе {city}:\nТемпература: {cur_weather:.0f} C° {wd}\n"
            f"Скорость ветра: {wind} m/c\n"
            f"Восход: {sunrise}\nЗакат: {sunset}\n"
            f"***Хорошего дня!***"
        )
        # print("message_reply", message_reply)
        return message_reply

    except Exception as e:
        print(e)
        message_reply = ("\U00002620 Проверьте навание города \U00002620")
        return message_reply
