from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def keyboard_gallery() -> ReplyKeyboardMarkup:
    """
    Инлайн клавиатура, прикрепляется к сообщению команды /gallery
    """
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🖊 Эскизы татуировок"),
             KeyboardButton(text="🎨 Рисунки")]
        ],
        input_field_placeholder="Выберите",
        resize_keyboard=True
    )
    return kb


def keyboard_gallery_tatoo() -> ReplyKeyboardMarkup:
    """
    Если пользователь нажал на кнопку ["🖊 Эскизы татуировок"], появляется эта клавиатура
    """
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="↩️ Вернуться"),
             KeyboardButton(text="🎨 Рисунки")]
        ],
        input_field_placeholder="Выберите",
        resize_keyboard=True
    )
    return kb


def keyboard_gallery_draw() -> ReplyKeyboardMarkup:
    """
    Если пользователь нажал на кнопку ["🎨 Рисунки"], появляется эта клавиатура
    """
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🖊 Эскизы татуировок"),
             KeyboardButton(text="↩️ Вернуться")]
        ],
        input_field_placeholder="Выберите",
        resize_keyboard=True
    )
    return kb