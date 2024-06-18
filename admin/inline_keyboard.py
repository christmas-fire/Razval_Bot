from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_admin_sending_mail() -> InlineKeyboardMarkup:
    """
    Инлайн клавиатура, при нажатии на кнопку отправляет сообщение всем пользователям
    """
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Отправить сообщение",
                                  callback_data="admin_sending_mail")]
        ]
    )
    return kb
