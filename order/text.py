def text_command_order() -> str:
    """
    Текст для команды /order
    """
    text = (f"Можете сделать заказ прямо в моем боте ✏️\n"
            f"Для этого следуйте инструкции ниже👇🏻\n\n"
            f"1. Укажите тип своей работы\n"
            f"2. Опишите детали заказа\n"
            f"3. По возможности прикрепите референсы (<b>до 10 шт.</b>)\n\n"
            f"Через пару дней я отпишусь вам в лс по поводу вашего заказа 💕")
    return text


def text_order_get_type() -> str:
    """
    Текст после нажатия на кнопку ["💸 Сделать заказ"]
    """
    text = (f"Укажите тип своей работы.\n"
            f"------\n"
            f"(Например: эскиз/портрет/рисунок)")
    return text


def text_order_get_details() -> str:
    """
    Текст после того как пользователь введет тип работы
    """
    text = f"Хорошо! Давайте перейдем к деталям"
    return text


def text_order_get_references() -> str:
    """
    Текст после того как пользователь введет детали заказа
    """
    text = f"Вас понял! Чтобы перейти к последнему шагу, ответьте: есть ли у вас референсы?"
    return text


def text_order_finish() -> str:
    """
    Текст после того как пользователь закончит делать заказ
    """
    text = (f"Готово! Ваш заказ отправлен на рассмотрение.\n"
            f"В скором времени ждите ответ 🙏🏻")
    return text


def text_order_summary(username, type_order, details_order) -> str:
    """
    Данные о заказе, которые прилетают админу/владельцу бота

    :param username: Имя пользователя в telegram
    :param type_order: Тип работы
    :param details_order: Детали заказа
    """
    text = (f"Пользователь @{username} сделал заказ:\n\n"
            f"------\n"
            f"Тип: {type_order}\n\n"
            f"Детали: {details_order}\n"
            f"------")
    return text


def text_order_references_for_razval_(username) -> str:
    """
    Референсы к заказу (если они есть), прилетают админу/владельцу бота

    :param username: Имя пользователя в telegram
    """
    text = f"Пользователь @{username} отправил референсы 👇🏻"
    return text