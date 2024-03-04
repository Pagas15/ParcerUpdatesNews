import json

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.config import MessageText, MONITORING_SITES_PATH

site_list_router = Router()


@site_list_router.message(Command('list'))
async def site_list_handler(message: Message):
    sites_details = []
    with open(MONITORING_SITES_PATH) as json_file:
        sites = json.load(json_file)['lists_sites']

    for site in sites.values():
        sites_details.append(f'{site["url"]} - {site["name"]} - {site["category"]}')

    await message.answer(text=MessageText.ALL_SITES_DETAILS.format(sites_details='\n'.join(sites_details)),
                         disable_web_page_preview=True)
