import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import bot
from agregate import aggregate_salaries
import json

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! Send me a JSON with the required data.")


@dp.message()
async def process_json(message: types.Message):
    try:
        data = json.loads(message.text)
        dt_from = data.get('dt_from')
        dt_upto = data.get('dt_upto')
        group_type = data.get('group_type')

        if not all([dt_from, dt_upto, group_type]):
            await message.reply(
                "JSON data is missing required fields:"
                " 'dt_from', 'dt_upto', 'group_type'"
            )
            return

        result = aggregate_salaries(dt_from, dt_upto, group_type)
        response = (f"Labels: {result['labels']}\n"
                    f"Dataset: {result['dataset']}")

        await bot.send_message(chat_id=message.chat.id, text=response)

    except json.JSONDecodeError:
        await message.reply(
            "Invalid JSON data. Please send a valid JSON."
        )
    except Exception as e:
        logging.error(
            f"An error occurred: {e}"
        )
        await message.reply(
            "An internal error occurred. Please try again later."
        )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
