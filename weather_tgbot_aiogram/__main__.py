import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from config import config
from handlers import *
from handlers.callback_handlers import get_weather_n_days_handler
from handlers.text_handlers import city
from services.inlinekeyboard import WeatherDaysCallbackFactory

router = Router()

# Создаем глобальную переменную, в которой указываем все команды и функции handlers из
# модуля handlers
COMMAND_HANDLERS = {
    "start": start_handler,
    "add_to_list": add_to_list,
    "show_list": show_list,
    "admin": admin_handler,
}


async def main() -> None:
    # Регистрируем comand handler с помощью словаря, содержащего ссылки на функции в
    # модуле handlers
    for command_name, command_handler in COMMAND_HANDLERS.items():
        router.message.register(command_handler, Command(command_name))

    # Регистрация функций, принимающей на вход текст от пользователя
    router.message.register(city, F.text)

    # Регистрация функций, принимающей на вход callback_data от InlineKeyboardButton
    router.callback_query.register(get_weather_n_days_handler,
                                   WeatherDaysCallbackFactory.filter())

    dp = Dispatcher()
    dp.include_router(router)

    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")

    mylist = [1, 2, 3]  # Вместо списка можно передать бд

    await dp.start_polling(bot, mylist=mylist)


if __name__ == '__main__':
    asyncio.run(main())
