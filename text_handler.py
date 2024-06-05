import random


'''Эмодзи из тг
🚀🔥💕🎉🤲🏻🎓✨✏️📖❤️🎨💫🖼🖊🎀👇🏻📎
'''

'''Форматирование html
    <b> - жирный текст
    <i> - курсивный текст
    <u> - подчеркнутый текст
'''

def text_command_start():
    text = f"<b>Добро пожаловать в мой уютный творческий уголок! 🤲🏻</b>\n\n\
Меня зовут Рина, я делаю <u>уникальные работы</u>, такие как \
вдохновляющие эскизы для татуировок и рисунки на различную тематику. \
Просто поделись своими идеями, и мы вместе сможем воплотить их в жизнь! 🎨💫\n\n\
Если у тебя есть какие-то вопросы или нужна помощь, не стесняйся спрашивать. \
Я здесь, чтобы помочь тебе раскрыть свой талант и вдохновиться новыми идеями. ✨🎉\n\n\
<b>Буду рада иметь с тобой дело!</b> 🎨✨"
    return text


def text_inline_start_contacts():
    text = f"<b>Мои контакты:</b>👇🏻\n\n\
        - <a href='https://t.me/razvalol' target='_self'>Перейти в тг</a>\n\
        - <a href='https://vk.com/razzvalll' target='_self'>Перейти в вк</a>"
    return text


def text_command_gallery():
    text = f"Здесь вы можете ознакомиться с примерами моих работ ✨"
    return text


def text_inline_gallery_tatoo():
    text = f"Вот мои эскизы! 🤲🏻"
    return text


def text_inline_gallery_draw():
    text = f"Вот мои рисунки! 🤲🏻"
    return text


def text_command_about():
    text = f"пум пум пум пум это я"
    return text


def text_command_order():
    text = f"Можете сделать заказ прямо в моем боте ✏️\n\
Для этого 👇🏻\n\n\
            1. Укажите тип своей работы\n\
            2. Опишите детали своего заказа\n\
            3. По возмножности прикрепите референсы\n\n\
Нажмите на кнопку <b>Сделать заказ</b> чтобы начать\n\
Через пару дней я отпишусь вам в лс по поводу вашего заказа 💕"
    return text


def text_order_type_for_user(type_order):
    text = f"<b>Тип работы</b>: {type_order}. Хорошо, давайте перейдем к деталям"
    return text


def text_order_type_for_razval(type_order, username):
    text_1 = f"<b>Пользователь @{username} сделал заказ</b> \n\n"
    text_2 = f"<b>Тип работы</b>: {type_order}"
    return text_1 + text_2
    