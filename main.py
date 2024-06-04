import asyncio
import logging
import sys

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode
from aiogram.utils.media_group import MediaGroupBuilder

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
    picture = FSInputFile("images/cat_start.jpg")
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
    

@dp.message(Command(commands=["gallery"]))
async def command_gallery(message: Message) -> None:
    picture = FSInputFile("images/cat_gallery.jpg")
    text = text_command_gallery()
    
    await message.answer_photo(picture, text, parse_mode=pm, reply_markup=inline_gallery())
    
    
@dp.callback_query(F.data.startswith("gallery_"))
async def callback_start(callback: CallbackQuery):
    action = callback.data.split("_")[1]
    
    if action == "tatoo":
        album = MediaGroupBuilder(caption=text_inline_gallery_tatoo())
        for i in range(1, 4):
            album.add_photo(media=FSInputFile(f"images/gallery_tatoo_{i}.jpg"))

        await callback.message.answer_media_group(media=album.build())
        await callback.message.answer(reply_markup=inline_gallery_if_tatoo(), text="------")
    
    elif action == "draw":
        album = MediaGroupBuilder(caption=text_inline_gallery_draw())
        for i in range(1, 4):
            album.add_photo(media=FSInputFile(f"images/gallery_draw_{i}.jpg"))

        await callback.message.answer_media_group(media=album.build())
        await callback.message.answer(reply_markup=inline_gallery_if_draw(), text="------")
        
    elif action == "back":
        await command_gallery(callback.message)
    
    await callback.answer()
    
    
async def main() -> None:
    await set_bot_commands(bot)
    await db_start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
