from aiogram import types


def get_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text="Текущая погода за оконом",
                                    callback_data="get_weather_now_handler")],
        [types.InlineKeyboardButton(text="Погода на день вперед",
                                    callback_data="get_weather_n_days_handler")],
        [types.InlineKeyboardButton(text="Погода на 3 дня вперед",
                                    callback_data="pass")],
        [types.InlineKeyboardButton(text="Погода на 5 дней вперед",
                                    callback_data="pass")],
        [types.InlineKeyboardButton(text="К начальному меню",
                                    callback_data="pass")],
    ]
    keybord = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keybord


async def get_weather_period_inlinekeyboard(message: types.Message, city):
    await message.answer(
        f"Выбери период, за который показать погоду в городе {city}:",
        reply_markup=get_keyboard()
    )
