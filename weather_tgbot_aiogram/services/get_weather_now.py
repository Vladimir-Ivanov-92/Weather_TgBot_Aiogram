from datetime import datetime
from enum import Enum
from typing import Literal, NamedTuple

import requests
from config import config
from exceptions.exceptions import GetWeatherServiceApiError
from models.pydantic_models import WeatherNowJson
from pydantic import ValidationError

# Алиасы значений
Celsius = int
Meters_per_second = int


class WeatherIcon(Enum):
    Thunderstorm = "\U000026A1"
    Drizzle = "\U00002614"
    Rain = "\U00002614"
    Snow = "\U0001F328"
    Clear = "\U00002600"
    Mist = "\U0001F32B"
    Clouds = "\U00002601"


class Weather(NamedTuple):
    temperature: Celsius
    wind: Meters_per_second
    weather_description: WeatherIcon
    sunrise: datetime
    sunset: datetime


def get_weather_now_new(city: str) -> Weather:
    """Requests weather in openweathermap.org API and return it"""
    open_weather_url = config.open_weather_url.format(
        city=city,
        open_weather_token=config.open_weather_token.get_secret_value()
    )
    openweather_response_data = _get_openweather_response_data(open_weather_url)
    weather = _parse_openweather_response_data(openweather_response_data)
    return weather


def _get_openweather_response_data(url: str) -> WeatherNowJson:
    r = requests.get(url)
    try:
        data = WeatherNowJson.parse_raw(r.content)
    except ValidationError:
        raise GetWeatherServiceApiError
    return data


def _parse_openweather_response_data(response_data: WeatherNowJson) -> Weather:
    return Weather(
        temperature=_parse_temperature(response_data),
        wind=_parse_wind(response_data),
        weather_description=_parse_weather_description(response_data),
        sunrise=_parse_sun_time(response_data, "sunrise"),
        sunset=_parse_sun_time(response_data, "sunset")
    )


def _parse_temperature(response_data: WeatherNowJson) -> Celsius:
    return round(response_data.main["temp"])


def _parse_wind(response_data: WeatherNowJson) -> Meters_per_second:
    return round(response_data.wind["speed"])


def _parse_weather_description(response_data: WeatherNowJson) -> WeatherIcon:
    try:
        weather_description_id = str(response_data.weather[0].id)
    except (IndexError, KeyError):
        raise GetWeatherServiceApiError
    print(weather_description_id)
    weather_description_dict = {
        "2": WeatherIcon.Thunderstorm,
        "3": WeatherIcon.Drizzle,
        "5": WeatherIcon.Rain,
        "6": WeatherIcon.Snow,
        "70": WeatherIcon.Mist,
        "800": WeatherIcon.Clear,
        "80": WeatherIcon.Clouds,
    }
    for _id, _weather_icon in weather_description_dict.items():
        if weather_description_id.startswith(_id):
            return _weather_icon
    raise GetWeatherServiceApiError


def _parse_sun_time(response_data: WeatherNowJson,
                    time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(response_data.sys[time])
