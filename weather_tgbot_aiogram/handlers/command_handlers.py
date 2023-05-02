from aiogram import types
from handlers import text_handlers
from keyboards.standard_keyboard import get_standart_city_keyboard


async def start_handler(message: types.Message):
    '''Функция обрабатывающая команду "/start" '''

    await message.answer(
        text="Укажи название города на английском и я расскажу о погоде в этом городе!\n"
             "Нажми /help чтоб ознакомиться с основными командами",
        reply_markup=get_standart_city_keyboard(),
    )


async def admin_handler(message: types.Message):
    '''Функция обрабатывающая команду "/admin" '''
    # buttons = [
    #     [types.InlineKeyboardButton(text="Показать словарь CITY",
    #                                 callback_data="get_weather_now_handler")],
    # ]
    # keybord_admin = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer(
        text=f"CITY: {text_handlers.CITY}",
    )
