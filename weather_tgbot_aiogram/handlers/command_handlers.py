from aiogram import types


async def start_handler(message: types.Message):
    '''Функция обрабатывающая команду "/start" '''

    keyboard_button = [
        [types.KeyboardButton(text="Saint Petersburg")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=keyboard_button,
        resize_keyboard=True,
        input_field_placeholder="Выберите город или введите название города "
                                "на английском!",
    )
    await message.answer(
        text="Укажи название города на английском и я расскажу о погоде в этом городе!\n"
             "Нажми /help чтоб ознакомиться с основными командами",
        reply_markup=keyboard,
    )
