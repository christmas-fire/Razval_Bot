import random


'''Эмодзи из тг
🚀🔥💕🎉🤲🏻🎓✨✏️📖❤️🎨💫🖼🖊🎀
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