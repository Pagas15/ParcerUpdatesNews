from aiogram import Router
from .admin_panel import admin_panel_router
from .callback.main import get_admin_callback_router
from bot.filters.is_admin import OnlyAdmin, OnlyAdminCallback

admin_router = Router()

admin_router.message.filter(OnlyAdmin())
admin_router.callback_query.filter(OnlyAdminCallback())


def get_admin_router() -> Router:
    admin_routers = (admin_panel_router, get_admin_callback_router(),)
    admin_router.include_routers(*admin_routers)
    return admin_router
