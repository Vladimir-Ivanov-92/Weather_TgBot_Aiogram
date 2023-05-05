from aiogram import Router, types
from keyboards.inlinekeyboard import WeatherDaysCallbackFactory
from services.get_format_weather import (format_weather_n_days,
                                         format_weather_now)
from services.get_weather_n_days_old import get_weather_n_days

STRING_FOR_STRIP = "Выбери период, за который показать погоду в городе:"

router = Router()


@router.callback_query(WeatherDaysCallbackFactory.filter())
async def get_weather_n_days_handler(callback: types.CallbackQuery,
                                     callback_data: WeatherDaysCallbackFactory):
    '''Функция обрабатывающая callback_data=WeatherDaysCallbackFactory'''

    city_from_callback = callback.message.text.strip(STRING_FOR_STRIP)

    if callback_data.days == 0:
        await callback.message.answer(format_weather_now(city_from_callback))
    elif callback_data.days == 1:
        await callback.message.answer(
            format_weather_n_days(city_from_callback, callback_data.interval))
    elif callback_data.days == 3:
        await callback.message.answer(
            get_weather_n_days(city_from_callback, callback_data.interval))
    elif callback_data.days == 5:
        await callback.message.answer(
            get_weather_n_days(city_from_callback, callback_data.interval))

    await callback.answer()
