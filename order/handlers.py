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
    typing_type = State()
    typing_details = State()
    sending_references = State()
    waiting_for_references = State()
    
    
@router_order.message(Command(commands=["order"]))
async def command_order(message: Message) -> None:
    picture = FSInputFile("images/cat_order.jpg")
    text = text_command_order()
    
    await message.answer_photo(picture, text, parse_mode=pm, reply_markup=inline_order())
    
    
@router_order.callback_query(StateFilter(None), F.data == "order_start")
async def callback_order_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Укажите тип своей работы")
    await state.set_state(Order.typing_type)
    await callback.answer()
    

@router_order.message(Order.typing_type)
async def get_type(message: Message, state: FSMContext) -> None:
    type_order = message.text
    username = message.from_user.username
    
    await message.answer(text_order_type_for_user(type_order), parse_mode=pm)
    await bot.send_message(chat_id=ADMIN, text=text_order_type_for_razval(type_order, username), parse_mode=pm)
    await state.set_state(Order.typing_details)


@router_order.message(Order.typing_details)
async def get_details(message: Message, state: FSMContext) -> None:
    details_order = message.text
    username = message.from_user.username
    
    await message.answer(text_order_details_for_user(details_order), parse_mode=pm, reply_markup=inline_order_details())
    await bot.send_message(chat_id=ADMIN, text=text_order_details_for_razval(details_order, username), parse_mode=pm)
    await state.set_state(Order.sending_references)


@router_order.callback_query(F.data == "order_without_references")
async def callback_order_finish_without_ref(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(text_order_finish())
    await callback.answer()


@router_order.callback_query(F.data == "order_with_references")
async def callback_order_finish_with_ref(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Пожалуйста, отправьте фотографии, которые хотите прикрепить к заказу.")
    await state.set_state(Order.waiting_for_references)
    await callback.answer()
    

@router_order.message(Order.waiting_for_references, F.content_type == ContentType.PHOTO)
async def handle_references(message: Message, state: FSMContext):
    if message.photo:
        data = await state.get_data()
        photos = data.get('photos', [])
        photos.append(message.photo[-1].file_id)
        
        await state.update_data(photos=photos)
        await message.answer("Фото получено. Отправьте еще фото или введите /done для завершения.")
        
    else:
        await message.answer("Пожалуйста, отправьте фотографию.")


@router_order.message(Order.waiting_for_references, Command(commands=["done"]))
async def finish_references(message: Message, state: FSMContext):
    data = await state.get_data()
    photos = data.get('photos', [])
    username = message.from_user.username
    
    if photos:
        album = MediaGroupBuilder()
        for file_id in photos:
            album.add_photo(media=file_id)
        
        await bot.send_media_group(chat_id=ADMIN, media=album.build())
        await bot.send_message(chat_id=ADMIN, text=text_order_references_for_razval(username), parse_mode=pm)
        await message.answer(text_order_finish())
    else:
        await message.answer("Вы не прикрепили ни одной фотографии.")
    
    await state.clear()