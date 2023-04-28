from aiogram import types
from services.inlinekeyboard import get_weather_period_inlinekeyboard

# Глобальная переменная запоминающая выбранный город для каждго пользователя по id.
CITY = {}


async def city(message: types.Message):  # TODO сделать проверку набранного польхователем города и если такого города нет сразу выводить сообщение об ошибке набора!
    '''Функция обрабатывающая входящий текст от пользователя '''

    city_from_user = message.text
    CITY[message.from_user.id] = city_from_user
    await get_weather_period_inlinekeyboard(message)
