from aiogram import Router
from .admin_panel import admin_panel_router
from .callback.main import get_admin_callback_router
from .site_list import site_list_router
from .faq import faq_router
from bot.filters.is_admin import OnlyAdmin, OnlyAdminCallback
from bot.filters.chat_type import ChatType
from bot.config import get_newsletter_chats_ids

admin_router = Router()

admin_router.message.filter(OnlyAdmin(), ChatType(chat_types=['private', 'supergroup'],
                                                  chats_id=[str(chat_id) for chat_id in get_newsletter_chats_ids()]))
admin_router.callback_query.filter(OnlyAdminCallback())


def get_admin_router() -> Router:
    admin_routers = (site_list_router, admin_panel_router, faq_router,
                     get_admin_callback_router())
    admin_router.include_routers(*admin_routers)
    return admin_router
