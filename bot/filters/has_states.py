import logging

from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import Message
from typing import List


class HasStates(BaseFilter):
    states: List[State] = []

    def __init__(self, states):
        self.states = states

    async def __call__(self, message: Message, state: FSMContext, *args, **kwargs):
        for state_item in self.states:
            if state_item == await state.get_state():
                return True

        return False
