from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode
from aiogram.utils.media_group import MediaGroupBuilder

from gallery.text import *
from gallery.inline_keyboard import *

router_gallery = Router()
pm = ParseMode.HTML


@router_gallery.message(Command(commands=["gallery"]))
async def command_gallery_handler(message: Message) -> None:
    """
    Обработчик команды /gallery
    """
    picture = FSInputFile("images/cat_gallery.jpg")
    text = text_command_gallery()
    
    await message.answer_photo(picture,
                               text,
                               parse_mode=pm,
                               reply_markup=inline_gallery())
    
    
@router_gallery.callback_query(F.data.startswith("gallery_"))
async def command_gallery_callback(callback: CallbackQuery) -> None:
    """
    Обработчик колбеков инлайн клавиатуры, прикрепленной к команде /gallery
    """
    action = callback.data.split("_")[1]
    
    if action == "tatoo":
        album = MediaGroupBuilder(caption=text_inline_gallery_tatoo())
        for i in range(1, 4):
            album.add_photo(media=FSInputFile(f"images/gallery_tatoo_{i}.jpg"))

        await callback.message.answer_media_group(media=album.build())
        await callback.message.answer(reply_markup=inline_gallery_if_tatoo(),
                                      text="ㅤ")  # Здесь используется "невидимый" символ
    
    elif action == "draw":
        album = MediaGroupBuilder(caption=text_inline_gallery_draw())
        for i in range(1, 4):
            album.add_photo(media=FSInputFile(f"images/gallery_draw_{i}.jpg"))

        await callback.message.answer_media_group(media=album.build())
        await callback.message.answer(reply_markup=inline_gallery_if_draw(),
                                      text="ㅤ")  # Здесь используется "невидимый" символ
        
    elif action == "back":
        await command_gallery_handler(callback.message)
    
    await callback.answer()