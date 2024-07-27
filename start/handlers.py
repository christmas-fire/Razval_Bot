import os

import dotenv
from aiogram import F, Router, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode

from start.text import *
from start.inline_keyboard import *
from sql_handler import *

router_start = Router()

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv("ADMIN")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@router_start.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    Обработчик команды /start
    """
    # await message.delete()
    picture = FSInputFile("images/cat_start.jpg")
    text = text_command_start()

    await message.answer_photo(picture,
                               text,
                               reply_markup=inline_start())
    await add_user(message.chat.id,
                   message.from_user.username,
                   message.from_user.first_name)
    await bot.send_message(chat_id=ADMIN,
                           text=f"🧑‍💻 Пользователь @{message.from_user.username} начал работу с ботом!")


@router_start.callback_query(F.data.startswith("start_"))
async def command_start_callback(callback: CallbackQuery) -> None:
    """
    Обработчик колбеков инлайн клавиатуры, прикрепленной к команде /start
    """
    action = callback.data.split("_")[1]
    text = text_inline_start_contacts()

    if action == "contacts":
        await callback.message.answer(text,
                                      disable_web_page_preview=True)
    await callback.answer()
