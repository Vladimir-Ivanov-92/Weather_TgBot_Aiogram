from aiogram import types
from aiogram.types import ReplyKeyboardMarkup


def get_standart_city_keyboard() -> ReplyKeyboardMarkup:
    keyboard_button = [
        [
            types.KeyboardButton(text="Saint Petersburg"),
        ],
    ]
    keyboard_with_city = types.ReplyKeyboardMarkup(
        keyboard=keyboard_button,
        resize_keyboard=True,
        input_field_placeholder="Выберите город или введите название города "
                                "на английском!",
    )
    return keyboard_with_city
