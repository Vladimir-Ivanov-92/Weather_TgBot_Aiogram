from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def weather_period_inlinekeyboard(message: types.Message, city):
    builder = InlineKeyboardBuilder()
    buttons = [
        types.InlineKeyboardButton(text="Текущая погода за оконом",
                                   callback_data="get_weather_now_handler"),
        types.InlineKeyboardButton(text="Погода на день вперед",
                                   callback_data="get_weather_n_days_handler"),
    ]

    builder.add(*buttons)
    await message.answer(
        f"Выбери период, за который показать погоду в городе {city}:",
        reply_markup=builder.as_markup()
    )
