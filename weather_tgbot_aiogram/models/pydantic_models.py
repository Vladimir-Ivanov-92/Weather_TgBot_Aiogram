from pydantic import BaseModel


class Weather(BaseModel):
    description: str
    icon: str
    id: int
    main: str


class WeatherNowJson(BaseModel):
    base: str
    clouds: dict
    cod: int
    coord: dict
    dt: int
    id: int
    main: dict
    name: str
    sys: dict
    timezone: int
    visibility: int
    weather: list[Weather]
    wind: dict


class ListWithWeather(BaseModel):
    clouds: dict
    dt: int
    dt_txt: str
    main: dict
    pop: int
    sys: dict
    visibility: int
    weather: list[Weather]
    wind: dict


class WeatherNDaysJson(BaseModel):
    city: dict
    cnt: int
    cod: str
    list: list[ListWithWeather]
