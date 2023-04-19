from aiogram import types
from services.get_weather_n_days import get_weather_n_days


async def weather_n_days_handler(message: types.Message, count: int = 8):
    await message.answer(get_weather_n_days(message.text, count))
