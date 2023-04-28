import requests
from config import config
from icon import code_to_smile, picture_time_of_day
from models.pydantic_models import WeatherNDaysJson


def get_weather_n_days(city, count: int = 8):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}"
                         f"&appid={config.open_weather_token.get_secret_value()}"
                         f"&units=metric&lang=ru&cnt={count}"
                         )

        data = WeatherNDaysJson.parse_raw(r.content)
        message_reply = []
        message_finaly = []

        for i in range(1, count, 2):
            city = data.city['name']
            date_and_time = data.list[i].dt_txt
            date = date_and_time.split(" ")[0]
            time = date_and_time.split(" ")[1]
            time_h_m = ":".join((time.split(":"))[:2])

            if time_h_m in picture_time_of_day:
                icon_time_of_day = picture_time_of_day[time_h_m]
            else:
                message_text = "Eror! icon_time_of_day"

            cur_weather = data.list[i].main['temp']
            weather_description = data.list[i].weather[0].main

            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                message_text = "Посмотри в окно! Не пойму что там происходит!"

            wind = data.list[i].wind["speed"]

            if time_h_m == "00:00" or time_h_m == "03:00":
                message_text = f"****<u>{date}</u>****"
                message_reply.append(message_text)

            message_text = (
                f"{icon_time_of_day} <u>{time_h_m}</u>\n"
                f"Температура: <b>{cur_weather:.0f}</b>C° {wd}\n"
                f"Скорость ветра: {wind:.0f} m/c\n"
            )
            message_reply.append(message_text)

            message_string = "\n".join(message_reply)
            message_finaly = (f"Погода в городе: <u>{city}</u>:\n"
                              f"{message_string}"
                              )
        return message_finaly
    except Exception as e:
        print(e)
        message_reply = ("\U00002620 Проверьте навание города \U00002620")
        return message_reply
