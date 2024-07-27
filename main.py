import asyncio
import logging
import sys
import os

import dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import types

from start.handlers import router_start
from gallery.handlers import router_gallery
from order.handlers import router_order
from admin.handlers import router_admin
from inline_mode import router_inline_mode

from default_commands import *
from sql_handler import *
from middleware import *

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv("ADMIN")
RAZVAL = os.getenv("RAZVAL")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.message.outer_middleware(BanMiddleware())


@dp.message(Command(commands=["sit_on_face"]))
async def sit_on_face(message: types.Message) -> None:
    await message.answer("Спасибо госпожа 🙏🏻")
    await bot.send_message(chat_id=RAZVAL,
                           text=f"Пользователь @{message.from_user.username} сел мне на лицо..")
    await bot.send_message(chat_id=ADMIN,
                           text=f"Пользователь @{message.from_user.username} сел мне на лицо..")


async def main() -> None:
    dp.include_routers(router_start,
                       router_gallery,
                       router_order,
                       router_admin,
                       router_inline_mode)
    await set_bot_commands(bot)
    await db_start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    """
    Отключить логирование при выгрузке на сервер (замедляет работу бота)
    """
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
