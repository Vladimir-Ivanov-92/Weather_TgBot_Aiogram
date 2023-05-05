from typing import List, NamedTuple

import requests
from config import config
from exceptions.exceptions import GetWeatherServiceApiError
from icon import WEATHER_DESCRIPTION_DICT, WeatherIcon
from models.pydantic_models import WeatherNDaysJson
from pydantic import ValidationError

# Алиасы значений
Celsius = int
Meters_per_second = int
Date_and_time = str


class WeatherNDays(NamedTuple):
    temperature: Celsius
    wind: Meters_per_second
    weather_description: WeatherIcon
    date: Date_and_time


def get_weather_n_days(city: str, count: int) -> List[WeatherNDays]:
    """Requests weather in openweathermap.org API and return it"""
    open_weather_url = config.open_weather_url_n_days.format(
        city=city,
        open_weather_token=config.open_weather_token.get_secret_value(),
        count=count
    )
    openweather_response_data = _get_openweather_response_data(open_weather_url)
    weather_list = []
    for period in range(1, count, 2):
        weather = _parse_openweather_response_data(openweather_response_data, period)
        weather_list.append(weather)
    return weather_list


def _get_openweather_response_data(url: str) -> WeatherNDaysJson:
    r = requests.get(url)
    try:
        data = WeatherNDaysJson.parse_raw(r.content)
    except ValidationError:
        raise GetWeatherServiceApiError
    return data


def _parse_openweather_response_data(response_data: WeatherNDaysJson,
                                     period: int) -> WeatherNDays:
    return WeatherNDays(
        temperature=_parse_temperature(response_data, period),
        wind=_parse_wind(response_data, period),
        weather_description=_parse_weather_description(response_data, period),
        date=_parse_data(response_data, period),
    )


def _parse_temperature(response_data: WeatherNDaysJson, period: int) -> Celsius:
    return round(response_data.list[period].main['temp'])


def _parse_wind(response_data: WeatherNDaysJson, period: int) -> Meters_per_second:
    return round(response_data.list[period].wind["speed"])


def _parse_weather_description(response_data: WeatherNDaysJson,
                               period: int) -> WeatherIcon:
    try:
        weather_description_id = str(response_data.list[period].weather[0].id)
    except (IndexError, KeyError):
        raise GetWeatherServiceApiError
    for _id, _weather_icon in WEATHER_DESCRIPTION_DICT.items():
        if weather_description_id.startswith(_id):
            return _weather_icon
    raise GetWeatherServiceApiError


def _parse_data(response_data: WeatherNDaysJson, period: int) -> Date_and_time:
    return response_data.list[period].dt_txt
