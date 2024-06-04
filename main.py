import asyncio
import logging
import sys

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

from text_handler import *
from default_commands import *
from inline_handler import *
from sql_handler import *

load_dotenv()

TOKEN = getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()
pm = ParseMode.HTML


@dp.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    picture = types.FSInputFile("images/cat_start.jpg")
    text = text_command_start()
    
    await message.answer_photo(picture, text, parse_mode=pm, reply_markup=inline_start())
    await add_user(message.chat.id, message.from_user.username, message.from_user.first_name)

@dp.callback_query(F.data.startswith("start_"))
async def callback_start(callback: CallbackQuery):
    action = callback.data.split("_")[1]
    
    text = text_inline_start_contacts()

    if action == "contacts":
        await callback.message.answer(text, parse_mode=pm, disable_web_page_preview=True)

    await callback.answer()
    
    
async def main() -> None:
    await set_bot_commands(bot)
    await db_start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
