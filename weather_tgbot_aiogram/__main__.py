import asyncio

from aiogram import Bot, Dispatcher
from config import config
from exceptions.exceptions import GetWeatherServiceApiError
from handlers import callback_handlers, command_handlers, text_handlers


async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")

    dp = Dispatcher()
    try:
        dp.include_routers(
            command_handlers.router,
            callback_handlers.router,
            text_handlers.router,
        )
    except GetWeatherServiceApiError:
        print("Не получилось получить данные о погоде!")

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
