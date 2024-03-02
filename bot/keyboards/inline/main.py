from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Inline:
    inline_buttons: List[List[InlineKeyboardButton]]
    markup: InlineKeyboardMarkup

    def __init__(self, buttons_list: List[List[InlineKeyboardButton]]):
        self.inline_buttons = buttons_list

    def get_markup(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=self.inline_buttons)


class InlineButtonText:
    pass
