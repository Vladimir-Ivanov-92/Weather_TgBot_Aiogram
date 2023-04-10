from aiogram import types


async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"Hello, <b>{message.from_user.first_name}</b>")
