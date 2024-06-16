from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, FSInputFile, ContentType
from aiogram.enums import ParseMode
from aiogram.utils.media_group import MediaGroupBuilder

from order.text import *
from order.inline_keyboard import *

load_dotenv()

TOKEN = getenv("TOKEN")
ADMIN = getenv("ADMIN")
RAZVAL = getenv("RAZVAL")

bot = Bot(TOKEN)
router_order = Router()
pm = ParseMode.HTML


class Order(StatesGroup):
    """
    Состояния заказа
    """
    typing_type = State()
    typing_details = State()
    sending_references = State()
    waiting_for_references = State()


@router_order.message(Command(commands=["order"]))
async def command_order_handler(message: Message) -> None:
    """
    Обработчик команды /order
    """
    picture = FSInputFile("images/cat_order.jpg")
    text = text_command_order()

    await message.answer_photo(picture,
                               text,
                               parse_mode=pm,
                               reply_markup=inline_order())


@router_order.callback_query(StateFilter(None), F.data == "order_start")
async def command_order_callback_start(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Устанавливает рабочее состояние заказа (получение типа)
    """
    await callback.message.answer(text_order_get_type())
    await state.set_state(Order.typing_type)
    await callback.answer()


@router_order.message(Order.typing_type)
async def command_order_callback_get_type(message: Message, state: FSMContext) -> None:
    """
    Получает тип заказа от пользователя и сохраняет эти данные -> переключает состояние (получение деталей)
    """
    type_order = message.text
    await state.update_data(type_order=type_order)
    await message.answer(text_order_get_details(),
                         parse_mode=pm)
    await state.set_state(Order.typing_details)


@router_order.message(Order.typing_details)
async def command_order_callback_get_details(message: Message, state: FSMContext) -> None:
    """
    Получает детали заказа от пользователя и сохраняет эти данные -> переключает состояние (есть ли референсы?)
    """
    details_order = message.text
    await state.update_data(details_order=details_order)

    await message.answer(text_order_get_references(),
                         parse_mode=pm,
                         reply_markup=inline_order_is_references())
    await state.set_state(Order.sending_references)


@router_order.callback_query(F.data == "order_without_references")
async def command_order_callback_finish_no_ref(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Если референсов нет, то собирает сохраненные данные от пользователя
     и отправляет их админу/владельцу бота, завершает заказ
    """
    data = await state.get_data()
    type_order = data.get('type_order')
    details_order = data.get('details_order')
    username = callback.from_user.username

    await bot.send_message(chat_id=RAZVAL,
                           text=text_order_summary(username, type_order, details_order),
                           parse_mode=pm)
    await callback.message.answer(text_order_finish())
    await state.clear()
    await callback.answer()


@router_order.callback_query(F.data == "order_with_references")
async def command_order_callback_finish_with_ref_begin(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Устанавливает состояние (получение референсов)
    """
    await callback.message.answer(f"Пожалуйста, отправьте фотографии, которые хотите прикрепить к заказу.")
    await state.set_state(Order.waiting_for_references)
    await callback.answer()


@router_order.message(Order.waiting_for_references, F.content_type == ContentType.PHOTO)
async def command_order_callback_handle_ref(message: Message, state: FSMContext) -> None:
    """
    Получает и сохраняет фотографии от пользователя
    """
    if message.photo:
        data = await state.get_data()
        photos = data.get('photos', [])
        photos.append(message.photo[-1].file_id)

        await state.update_data(photos=photos)
        await message.answer(f"Фото получено.\n"
                             f"Отправьте еще фото или введите /done для завершения.")

    else:
        await message.answer(f"Пожалуйста, отправьте фотографию.")


@router_order.message(Order.waiting_for_references, Command(commands=["done"]))
async def command_order_callback_finish_with_ref_end(message: Message, state: FSMContext) -> None:
    """
    Если референсы есть, то собирает сохраненные данные от пользователя
     и отправляет их админу/владельцу бота, завершает заказ
    """
    data = await state.get_data()
    photos = data.get('photos', [])
    type_order = data.get('type_order')
    details_order = data.get('details_order')
    username = message.from_user.username

    if photos:
        album = MediaGroupBuilder()
        for file_id in photos:
            album.add_photo(media=file_id)

        await bot.send_message(chat_id=RAZVAL,
                               text=text_order_summary(username, type_order, details_order),
                               parse_mode=pm)
        await bot.send_message(chat_id=RAZVAL,
                               text=text_order_references_for_razval_(username),
                               parse_mode=pm)
        await bot.send_media_group(chat_id=RAZVAL,
                                   media=album.build())
        await message.answer(text_order_finish())
    else:
        await message.answer(f"Вы не прикрепили ни одной фотографии.")

    await state.clear()