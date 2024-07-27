import os
import dotenv

from aiogram import Bot, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode

from admin.keyboard import keyboard_admin
from admin.inline_keyboard import inline_admin_sending_mail
from sql_handler import get_users_id, get_users_username, get_orders_username
from middleware import banned_users

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN = int(os.getenv("ADMIN"))
RAZVAL = int(os.getenv("RAZVAL"))

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
router_admin = Router()


class Mail(StatesGroup):
    """
    Состояния рассылки
    """
    typing_mail = State()
    sending_mail = State()


@router_admin.message(Command(commands=["admin"]))
async def admin_console(message: Message) -> None:
    """
    Обработчик команды /admin
    """
    await message.delete()
    if message.from_user.id == ADMIN or message.from_user.id == RAZVAL:
        await message.answer("Вы перешли в режим админа!",
                             reply_markup=keyboard_admin())
    else:
        await message.answer("Вам сюда нельзя..")


# region [💬 Рассылка]
@router_admin.message(StateFilter(None), lambda message: message.text == "💬 Рассылка")
async def admin_start_mail(message: Message, state: FSMContext) -> None:
    """
    Обработчик кнопки [💬 Рассылка], переключает состояние на "пишет сообщение..."
    """
    await message.delete()
    await message.answer(f"Вы вошли в меню <b>[💬 Рассылка]</b>.\n"
                         f"Для отправки сообщения всем пользователям:\n\n"
                         f"1. ✏️ Введите свое сообщение\n"
                         f"2. 🤖 Дождитесь ответа от бота\n"
                         f"3. 📩 Нажмите на кнопку для отправки сообщения")
    await message.answer("Введите сообщение:")
    await state.set_state(Mail.typing_mail)


@router_admin.message(Mail.typing_mail)
async def admin_typing_mail(message: Message, state: FSMContext) -> None:
    """
    Получает сообщение от админа, переключает состояние на "отправляет сообщение..."
    """
    to_mail = message.text
    await state.update_data(to_mail=to_mail)
    await message.answer("Сообщение получено и готово к отправке!",
                         reply_markup=inline_admin_sending_mail())
    await state.set_state(Mail.sending_mail)


@router_admin.callback_query(Mail.sending_mail, F.data == "admin_sending_mail")
async def admin_sending_mail(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Отправляет сообщение всем пользователям из БД
    """
    data = await state.get_data()
    text = data.get("to_mail")
    users = await get_users_id()
    for user in users:
        user_id = user[0]
        try:
            await bot.send_message(chat_id=user_id,
                                   text=text)
            await state.clear()
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")
    await callback.answer("Сообщение отправлено!")


# endregion [💬 Рассылка]


# region [🐔 Заблокированные пользователи]
@router_admin.message(lambda message: message.text == "🐔 Заблокированные пользователи")
async def admin_banlist(message: Message) -> None:
    """
    Список заблокированных пользователей
    """
    await message.delete()
    text = f"🐔 Заблокированные пользователи:\n\n"
    count = 1
    for i in banned_users.keys():
        username = banned_users.get(i)
        text += f"{count}. @{username}\n"
        count += 1
    await message.answer(text)
# endregion [🐔 Заблокированные пользователи]


# region [👤 Список пользователей]
@router_admin.message(lambda message: message.text == "👤 Список пользователей")
async def list_of_users(message: Message) -> None:
    """
    Список пользователей
    """
    await message.delete()
    text = f"👤 Список пользователей:\n\n"
    count = 1
    users = await get_users_username()
    for user in users:
        user_username = user[0]
        text += f"{count}. @{user_username}\n"
        count += 1
    await message.answer(text)
# endregion [👤 Список пользователей]


# region [📚 Список заказов]
@router_admin.message(lambda message: message.text == "📚 Список заказов")
async def list_of_orders(message: Message) -> None:
    """
    Список пользователей, которые сделали заказ
    """
    await message.delete()
    text = f"📚 Список пользователей, которые сделали заказ:\n\n"
    count = 1
    orders = await get_orders_username()
    for order in orders:
        order_username = order[0]
        text += f"{count}. @{order_username}\n"
        count += 1
    await message.answer(text)
# endregion [📚 Список заказов]