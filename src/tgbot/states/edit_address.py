from aiogram.dispatcher.filters.state import State, StatesGroup


class EditAddressState(StatesGroup):
    WaitingForAddress = State()
