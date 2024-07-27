from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_start() -> InlineKeyboardMarkup:
    """
    Инлайн клавиатура, прикрепляется к сообщению команды /start
    """
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📞 Мои контакты",
                                  callback_data="start_contacts")],
            [InlineKeyboardButton(text="📎 Мой сайт",
                                  url="https://ru.pinterest.com/pin/280700989269081408/")]
        ]
    )
    return kb