from typing import Optional

from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers import text_handlers


class WeatherDaysCallbackFactory(CallbackData, prefix='get_weather'):
    days: int
    interval: Optional[int]


def get_inline_weather_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Текущая погода за окном",
                    callback_data=WeatherDaysCallbackFactory(days=0)),
    keyboard.button(text="Погода на день вперед",
                    callback_data=WeatherDaysCallbackFactory(days=1, interval=8)),
    keyboard.button(text="Погода на 3 дня вперед",
                    callback_data=WeatherDaysCallbackFactory(days=1, interval=24)),
    keyboard.button(text="Погода на 5 дней вперед",
                    callback_data=WeatherDaysCallbackFactory(days=1, interval=40)),
    # builder.button(text="К начальному меню", callback_data=WeatherDaysCallbackFactory(days=1)),
    keyboard.adjust(1)
    return keyboard.as_markup()


async def get_weather_period_from_inlinekeyboard(message: types.Message):
    city = text_handlers.CITY[message.from_user.id]
    await message.answer(
        f"Выбери период, за который показать погоду в городе {city}:",
        reply_markup=get_inline_weather_keyboard()
    )
