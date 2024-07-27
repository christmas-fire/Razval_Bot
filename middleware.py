from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


banned_users = {
    627148614: 'whyhwahee',
    719571990: 'AnotherPumpkin',
    1979214166: 'horisana'
}


def is_banned(user_id) -> bool:
    """
    Функция проверяет, находится ли пользователь в банлисте

    :param user_id: id пользователя в telegram
    """
    return user_id in banned_users


def text_if_banned():
    """
    Текст, который видит заблокированный пользователь при попытке использования бота
    """
    text = "Вы наказаны за свое плохое поведение! ✨"
    return text


class BanMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        user_id = event.from_user.id
        if user_id in banned_users:
            await event.answer(text_if_banned())
            return
        result = await handler(event, data)
        return result
