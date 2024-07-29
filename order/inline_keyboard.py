from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_order() -> InlineKeyboardMarkup:
    """
    Инлайн клавиатура, прикрепляется к сообщению команды /order
    """
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💸 Сделать заказ",
                                  callback_data="order_start")]
        ]
    )
    return kb


def inline_order_is_references() -> InlineKeyboardMarkup:
    """
    Инлайн клавиатура, вылезает в момент уточнения наличия референсов у заказчика
    """
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Есть",
                                  callback_data="order_with_references"),
             InlineKeyboardButton(text="❌ Нет",
                                  callback_data="order_without_references")]
        ]
    )
    return kb
