from typing import Optional

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


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
