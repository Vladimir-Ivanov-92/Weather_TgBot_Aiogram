from aiogram import types
from services.get_weather_n_days import get_weather_n_days
from services.get_weather_now import get_weather_now
from keyboards.inlinekeyboard import WeatherDaysCallbackFactory

STRING_FOR_STRIP = "Выбери период, за который показать погоду в городе:"


async def get_weather_n_days_handler(callback: types.CallbackQuery,
                                     callback_data: WeatherDaysCallbackFactory):
    '''Функция обрабатывающая callback_data=WeatherDaysCallbackFactory'''

    city_from_callback = callback.message.text.strip(STRING_FOR_STRIP)

    if callback_data.days == 0:
        await callback.message.answer(get_weather_now(city_from_callback))
    elif callback_data.days == 1:
        await callback.message.answer(
            get_weather_n_days(city_from_callback, callback_data.interval))
    elif callback_data.days == 3:
        await callback.message.answer(
            get_weather_n_days(city_from_callback, callback_data.interval))
    elif callback_data.days == 5:
        await callback.message.answer(
            get_weather_n_days(city_from_callback, callback_data.interval))

    await callback.answer()
