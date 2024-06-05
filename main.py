import asyncio
import logging
import sys

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from aiogram.enums import ParseMode
from aiogram.utils.media_group import MediaGroupBuilder

from start.inline_keyboard import *
from start.text import *

from gallery.inline_keyboard import *
from gallery.text import *

from about.text import *

from order.inline_keyboard import *
from order.text import *

from default_commands import *
from sql_handler import *

load_dotenv()

TOKEN = getenv("TOKEN")
ADMIN = getenv("ADMIN")
RAZVAL = getenv("RAZVAL")

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
    
    
    '''
    ----------------------------------------------Поменять текст
    '''
@dp.message(Command(commands=["about"]))
async def command_about(message: Message) -> None:
    picture = FSInputFile("images/cat_about.jpg")
    text = text_command_about()
    
    await message.answer_photo(picture, text, parse_mode=pm)
    
    
class Order(StatesGroup):
    typing_type = State()
    typing_details = State()
    sending_references = State()
    
    
@dp.message(Command(commands=["order"]))
async def command_order(message: Message) -> None:
    picture = FSInputFile("images/cat_order.jpg")
    text = text_command_order()
    
    await message.answer_photo(picture, text, parse_mode=pm, reply_markup=inline_order())
    
    
@dp.callback_query(StateFilter(None), F.data == "order_start")
async def callback_order_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Укажите тип своей работы")
    await state.set_state(Order.typing_type)
    await callback.answer()
    

@dp.message(Order.typing_type)
async def get_type(message: Message, state: FSMContext) -> None:
    type_order = message.text
    username = message.from_user.username
    
    await message.answer(text_order_type_for_user(type_order), parse_mode=pm)
    await bot.send_message(chat_id=ADMIN, text=text_order_type_for_razval(type_order, username), parse_mode=pm)
    await state.set_state(Order.typing_details)
    

@dp.message(Order.typing_details)
async def get_details(message: Message, state: FSMContext) -> None:
    details_order = message.text
    username = message.from_user.username
    
    await message.answer(text_order_details_for_user(details_order), parse_mode=pm, reply_markup=inline_order_details())
    await state.set_state(Order.sending_references)
    
    
@dp.callback_query(F.data == "order_without_references")
async def callback_order_finish(callback: CallbackQuery, state: FSMContext) -> None:
    pass
    

async def main() -> None:
    await set_bot_commands(bot)
    await db_start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
