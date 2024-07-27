from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.enums import ParseMode
from aiogram.utils.media_group import MediaGroupBuilder

from gallery.text import *
from gallery.keyboard import *

router_gallery = Router()
pm = ParseMode.HTML


@router_gallery.message(Command(commands=["gallery"]))
async def command_gallery_handler(message: Message) -> None:
    """
    Обработчик команды /gallery
    """
    await message.delete()
    picture = FSInputFile("images/cat_gallery.jpg")
    text = text_command_gallery()

    await message.answer_photo(picture,
                               text,
                               reply_markup=keyboard_gallery())


@router_gallery.message(lambda message: message.text == "🖊 Эскизы татуировок")
async def command_gallery_tatoo(message: Message) -> None:
    await message.delete()
    album = MediaGroupBuilder()
    for i in range(1, 4):
        album.add_photo(media=FSInputFile(f"images/gallery_tatoo_{i}.jpg"))

    await message.answer_media_group(media=album.build())
    await message.answer(reply_markup=keyboard_gallery_tatoo(),
                         text=text_inline_gallery_tatoo())


@router_gallery.message(lambda message: message.text == "🎨 Рисунки")
async def command_gallery_tatoo(message: Message) -> None:
    await message.delete()
    album = MediaGroupBuilder()
    for i in range(1, 4):
        album.add_photo(media=FSInputFile(f"images/gallery_draw_{i}.jpg"))

    await message.answer_media_group(media=album.build())
    await message.answer(reply_markup=keyboard_gallery_draw(),
                         text=text_inline_gallery_draw())


@router_gallery.message(lambda message: message.text == "↩️ Вернуться")
async def command_gallery_tatoo(message: Message) -> None:
    await command_gallery_handler(message)
