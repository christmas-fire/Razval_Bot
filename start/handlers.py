from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode

from start.text import *
from start.inline_keyboard import *
from sql_handler import *

router_start = Router()
pm = ParseMode.HTML


@router_start.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
        
    picture = FSInputFile("images/cat_start.jpg")
    text = text_command_start()
    
    await message.answer_photo(picture, text, parse_mode=pm, reply_markup=inline_start())
    await add_user(message.chat.id, message.from_user.username, message.from_user.first_name)
    

@router_start.callback_query(F.data.startswith("start_"))
async def callback_start(callback: CallbackQuery):
    action = callback.data.split("_")[1]
    text = text_inline_start_contacts()

    if action == "contacts":
        await callback.message.answer(text, parse_mode=pm, disable_web_page_preview=True)
        
    await callback.answer()