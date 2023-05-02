from aiogram import types
from handlers import text_handlers
from keyboards.inlinekeyboard import get_inline_weather_keyboard


async def get_weather_period_from_inlinekeyboard(message: types.Message):
    city = text_handlers.CITY[message.from_user.id]
    await message.answer(
        f"Выбери период, за который показать погоду в городе {city}:",
        reply_markup=get_inline_weather_keyboard()
    )
