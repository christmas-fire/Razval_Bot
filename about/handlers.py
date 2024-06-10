from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.enums import ParseMode

from about.text import *

router_about = Router()
pm = ParseMode.HTML


@router_about.message(Command(commands=["about"]))
async def command_about(message: Message) -> None:
    picture = FSInputFile("images/cat_about.jpg")
    text = text_command_about()

    await message.answer_photo(picture, text, parse_mode=pm)