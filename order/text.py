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
    text = f"Хорошо! Давайте перейдем к деталям"
    return text


def text_order_type_for_razval(type_order, username):
    text_1 = f"<b>Пользователь @{username} сделал заказ</b> \n\n"
    text_2 = f"<b>Тип работы</b>: {type_order}"
    return text_1 + text_2

def text_order_details_for_user(details_order):
    text = f"Вас понял! Чтобы перейти к последнему шагу, ответьте: есть ли у вас референсы?"
    return text


def text_order_details_for_razval(details_order, username):
    text_1 = f"<b>Пользователь @{username} сделал заказ</b> \n\n"
    text_2 = f"<b>Детали</b>: {details_order}"
    return text_1 + text_2


def text_order_finish():
    text = f"Готово! Ваш заказ отправлен на рассмотрение.\nВ скором времени ждите ответ 🙏🏻"
    return text