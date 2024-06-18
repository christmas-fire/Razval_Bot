from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode

from admin.keyboard import keyboard_admin
from admin.inline_keyboard import inline_admin_sending_mail
from sql_handler import get_users
from middleware import banned_users

load_dotenv()

TOKEN = getenv("TOKEN")

bot = Bot(TOKEN)
router_admin = Router()
pm = ParseMode.HTML


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
    await message.answer("Вы перешли в режим админа!",
                         reply_markup=keyboard_admin())


#region [💬 Рассылка]
@router_admin.message(StateFilter(None), lambda message: message.text == "💬 Рассылка")
async def admin_start_mail(message: Message, state: FSMContext) -> None:
    await message.answer(f"Вы вошли в меню <b>Рассылка</b>.\n"
                         f"Для отправки сообщения всем пользователям:\n\n"
                         f"1. Введите свое сообщение\n"
                         f"2. Отправьте его",
                         parse_mode=pm)
    await message.answer("Введите сообщение:")
    await state.set_state(Mail.typing_mail)


@router_admin.message(Mail.typing_mail)
async def admin_typing_mail(message: Message, state: FSMContext) -> None:
    to_mail = message.text
    await state.update_data(to_mail=to_mail)
    await message.answer("Сообщение получено и готово к отправке",
                         reply_markup=inline_admin_sending_mail())
    await state.set_state(Mail.sending_mail)


@router_admin.callback_query(Mail.sending_mail, F.data == "admin_sending_mail")
async def admin_sending_mail(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    text = data.get("to_mail")
    users = await get_users()
    for user in users:
        user_id = user[0]
        try:
            await bot.send_message(chat_id=user_id,
                                   text=text,
                                   parse_mode=pm)
            await state.clear()
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")
    await callback.answer("Сообщение отправлено!")


#endregion [💬 Рассылка]


#region [🐔 Заблокированные пользователи]
@router_admin.message(lambda message: message.text == "🐔 Заблокированные пользователи")
async def admin_banlist(message: Message) -> None:
    text = f"Вот список заблокированных пользователей:\n\n"
    count = 1
    for i in banned_users.keys():
        username = banned_users.get(i)
        text += f"{count}. @{username}\n"
        count += 1
    await message.answer(text,
                         parse_mode=pm)
#endregion [🐔 Заблокированные пользователи]
