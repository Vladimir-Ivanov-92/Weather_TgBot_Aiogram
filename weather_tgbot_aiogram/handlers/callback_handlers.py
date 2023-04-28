from aiogram import types
from services.get_weather_n_days import get_weather_n_days
from services.get_weather_now import get_weather_now

STRING_FOR_STRIP = "Выбери период, за который показать погоду в городе:"


async def get_weather_now_handler(callback: types.CallbackQuery):
    '''Функция обрабатывающая callback_data="get_weather_now_handler" '''

    city_from_callback = callback.message.text.strip(STRING_FOR_STRIP)
    await callback.message.answer(get_weather_now(city_from_callback))
    await callback.answer()


async def get_weather_n_days_handler(callback: types.CallbackQuery):
    '''Функция обрабатывающая callback_data="get_weather_n_days_handler" '''

    city_from_callback = callback.message.text.strip(STRING_FOR_STRIP)
    await callback.message.answer(get_weather_n_days(city_from_callback, 8))
    await callback.answer()
