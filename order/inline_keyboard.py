from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_order() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Сделать заказ", callback_data="order_start")]
        ]
    )
    return kb