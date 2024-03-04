from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.config import MessageText

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=MessageText.NO_PERMISSION)
