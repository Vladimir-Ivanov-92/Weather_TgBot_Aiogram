from pydantic import BaseModel


class Weather(BaseModel):
    description: str
    icon: str
    id: int
    main: str


class OpenWeatherJson(BaseModel):
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
