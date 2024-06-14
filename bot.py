import asyncio
import logging
from aiogram import Dispatcher, types
from aiogram.filters.command import Command
from config import bot

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
