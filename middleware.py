from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

banned_users = [
    627148614, # whyhwahee
    719571990, # AnotherPumpkin
    1979214166 # horisana
]

def is_banned(user_id) -> bool:
    return user_id in banned_users


def text_if_banned():
    text = "Вы наказаны за свое плохое поведение! ✨"
    return text


class BanMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler,
                       event: TelegramObject,
                       data) -> Any:
        user_id = event.from_user.id
        if user_id in banned_users:
            await event.answer("СЪЕБАЛ С ЛОБАКА")
            return
        result = await handler(event, data)
        return result