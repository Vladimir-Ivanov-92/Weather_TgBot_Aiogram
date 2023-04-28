from aiogram import types
from handlers import text_handlers


async def start_handler(message: types.Message):
    '''Функция обрабатывающая команду "/start" '''

    keyboard_button = [
        [types.KeyboardButton(text="Saint Petersburg")]
    ]
    keyboard_start = types.ReplyKeyboardMarkup(
        keyboard=keyboard_button,
        resize_keyboard=True,
        input_field_placeholder="Выберите город или введите название города "
                                "на английском!",
    )
    await message.answer(
        text="Укажи название города на английском и я расскажу о погоде в этом городе!\n"
             "Нажми /help чтоб ознакомиться с основными командами",
        reply_markup=keyboard_start,
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
