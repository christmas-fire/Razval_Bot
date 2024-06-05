from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_gallery() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🖊Эскизы татуировок", callback_data="gallery_tatoo"),
            InlineKeyboardButton(text="🎨Рисунки", callback_data="gallery_draw")]
        ]
    )
    return kb


def inline_gallery_if_tatoo() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="◀️Вернуться", callback_data="gallery_back"),
             InlineKeyboardButton(text="🎨Рисунки", callback_data="gallery_draw")]
        ]
    )
    return kb


def inline_gallery_if_draw() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="◀️Вернуться", callback_data="gallery_back"),
             InlineKeyboardButton(text="🖊Эскизы татуировок", callback_data="gallery_tatoo")]
        ]
    )
    return kb