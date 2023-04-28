from aiogram import types
from services.inlinekeyboard import get_weather_period_inlinekeyboard

# Глобальная переменная запоминающая выбранный город.
CITY = None  # TODO заменить на локальную переменную для пользователя


async def city(message: types.Message):  # TODO сделать проверку набранного польхователем города и если такого города нет сразу выводить сообщение об ошибке набора!
    '''Функция обрабатывающая входящий текст от пользователя '''

    CITY = message.text
    await get_weather_period_inlinekeyboard(message, CITY)
