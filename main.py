import asyncio
import logging
import sys

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from start.handlers import router_start
from gallery.handlers import router_gallery
from about.handlers import router_about
from order.handlers import router_order
from admin.handlers import router_admin

from default_commands import *
from sql_handler import *
from middleware import *

load_dotenv()

TOKEN = getenv("TOKEN")
ADMIN = getenv("ADMIN")
RAZVAL = getenv("RAZVAL")

bot = Bot(TOKEN)
dp = Dispatcher()

dp.message.outer_middleware(BanMiddleware())


async def main() -> None:
    dp.include_routers(router_start,
                       router_gallery,
                       router_about,
                       router_order,
                       router_admin)
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