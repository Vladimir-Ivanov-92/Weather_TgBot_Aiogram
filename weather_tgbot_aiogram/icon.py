from enum import Enum


class WeatherIcon(Enum):
    Thunderstorm = "\U000026A1"
    Drizzle = "\U00002614"
    Rain = "\U00002614"
    Snow = "\U0001F328"
    Clear = "\U00002600"
    Mist = "\U0001F32B"
    Clouds = "\U00002601"


WEATHER_DESCRIPTION_DICT = {
    "2": WeatherIcon.Thunderstorm,
    "3": WeatherIcon.Drizzle,
    "5": WeatherIcon.Rain,
    "6": WeatherIcon.Snow,
    "70": WeatherIcon.Mist,
    "800": WeatherIcon.Clear,
    "80": WeatherIcon.Clouds,
}

PICTURES_TIME_OF_DAY = {
    "00:00": "\U0001F303(Ночь)",
    "03:00": "\U0001F303(Ночь)",
    "06:00": "\U0001F305(Утро)",
    "09:00": "\U0001F305(Утро)",
    "12:00": "\U0001F306(День)",
    "15:00": "\U0001F306(День)",
    "18:00": "\U0001F307(Вечер)",
    "21:00": "\U0001F307(Вечер)",
}
