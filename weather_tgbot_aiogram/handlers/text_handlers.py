import requests
from aiogram import F, Router, types
from config import config
from services.get_weather_period import get_weather_period_from_inlinekeyboard

# Глобальная переменная запоминающая выбранный город для каждго пользователя по id.
# TODO: заменить переменную на поля в БД
CITY = {}

router = Router()


@router.message(F.text)
async def city(message: types.Message):
    '''Функция обрабатывающая входящий текст от пользователя '''

    city_from_user = message.text
    # Проверка правильности введеного пользователем города и возможности получить данные
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_from_user}"
        f"&appid={config.open_weather_token.get_secret_value()}"
        "&units=metric&lang=ru"
    )
    if r.status_code != 200:
        print(f"status cod:{r.status_code}, message: {r.json()['message']}")
        await message.answer(text=r.json()['message'])
    else:
        CITY[message.from_user.id] = city_from_user
        await get_weather_period_from_inlinekeyboard(message)
