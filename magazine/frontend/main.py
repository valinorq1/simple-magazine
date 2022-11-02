import asyncio
import os

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
)
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData

TOKEN = "5669319191:AAFYiHFkIwIQaxe6ZbeLCpMN8JJUTbvpIdI"
ADMIN = 647310559

loop = asyncio.get_event_loop()

bot = Bot(token=TOKEN, loop=loop, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

moder_cb = CallbackData("moder", "action", "id")


def admin_keyboard() -> ReplyKeyboardMarkup:
    """Стартовая клавиатура для админов"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        *[KeyboardButton(name) for name in ["☎ Клиенты", "📄 Сессии", "🐝 Модеры"]]
    )
    keyboard.add(
        *[KeyboardButton(name) for name in ["♻ Настройки", "📳 Оповещения", "📜 Отчёты"]]
    )
    keyboard.add(*[KeyboardButton(name) for name in ["Подготовка сессий", "Прокси"]])

    keyboard.add(*[KeyboardButton(name) for name in ["📧 Написать всем", "💲 Финансы"]])
    return keyboard


@dp.message_handler(commands=["admin"])
async def cmd_start(message: Message):
    await message.reply(
        "Добро пожаловать в админ панель", reply_markup=admin_keyboard()
    )


async def get_button():
    data = ["pasha", "misha", "lesha"]
    buttons = []
    for i in data:
        buttons.append(
            InlineKeyboardButton(
                f"🐝 {i}",
                callback_data=moder_cb.new(action="select_moder", id=i),
            )
        )
    keyboard = InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(Text(equals=["🐝 Модеры"]))
async def show_moder_kb(message: Message):
    markup = await get_button()
    print(markup)
    await message.reply("Список активных модераторов", reply_markup=markup)  # type: ignore


executor.start_polling(dp, skip_updates=True)
