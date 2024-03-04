from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.config import MessageText

faq_router = Router()


@faq_router.message(Command('faq'))
async def faq_handler(message: Message):
    await message.answer(text=MessageText.FAQ)
