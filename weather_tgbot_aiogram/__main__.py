import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from config import config
from handlers import *

router = Router()

# Создаем глобальную переменную, в которой указываем все команды и функции handlers из
# пакета handlers
COMMAND_HANDLERS = {
    "start": command_start_handler,
    "weather": weather,
    "add_to_list": add_to_list,
    "show_list": show_list
}


async def main() -> None:
    # Регистрируем router для всех handler с помощью словаря, содержащего ссылки
    # на функции в модуле handlers
    for command_name, command_handler in COMMAND_HANDLERS.items():
        router.message.register(command_handler, Command(command_name))

    dp = Dispatcher()
    dp.include_router(router)

    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")

    mylist = [1, 2, 3]  # Вместо списка можно передать бд?

    await dp.start_polling(bot, mylist=mylist)


if __name__ == '__main__':
    asyncio.run(main())
