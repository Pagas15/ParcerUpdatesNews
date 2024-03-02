from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

admin_panel_router = Router()


@admin_panel_router.message(Command(commands=['admin']))
async def admin_panel_handler(message: Message):
    await message.answer(text='admin panel')
