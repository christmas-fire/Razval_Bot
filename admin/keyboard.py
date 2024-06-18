from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def keyboard_admin() -> ReplyKeyboardMarkup:
    """
    Клавиатура, которая появляется при введении команды /admin
    """
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💬 Рассылка"), KeyboardButton(text="🐔 Заблокированные пользователи")]
        ],
        input_field_placeholder="Выберите",
        resize_keyboard=True
    )
    return kb
