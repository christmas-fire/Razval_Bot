from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_start() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📞Мои контакты", callback_data="start_contacts")],
            [InlineKeyboardButton(text="📎Сайт с примерами работ", url="https://ru.pinterest.com/pin/280700989269081408/")]
        ]
    )
    return kb