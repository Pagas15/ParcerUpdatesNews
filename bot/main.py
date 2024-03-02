import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from bot.handlers.main import get_all_routers

from bot.config import BOT_TOKEN

dp = Dispatcher(storage=RedisStorage(Redis(host=os.getenv('REDIS_HOST'))))


async def start_bot():
    dp.include_routers(*get_all_routers())
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
