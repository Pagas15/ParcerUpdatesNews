from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.config import MessageText, get_monitoring_sites

site_list_router = Router()


@site_list_router.message(Command('list'))
async def site_list_handler(message: Message):
    sites_details = []
    sites = get_monitoring_sites()

    for site in sites['lists_sites'].values():
        sites_details.append(f'{site["url"]} - {site["name"]} - {site["category"]}')

    for site in sites['every_tick_sites'].values():
        sites_details.append(f'{site["url"]} - {site["name"]} - {site["category"]}')

    await message.answer(text=MessageText.ALL_SITES_DETAILS.format(sites_details='\n'.join(sites_details)),
                         disable_web_page_preview=True)
