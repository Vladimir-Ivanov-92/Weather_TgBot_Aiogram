from aiogram import types
from services.get_weather_now import get_weather_now


async def weather(message: types.Message):
    await message.answer(get_weather_now(message.text))
