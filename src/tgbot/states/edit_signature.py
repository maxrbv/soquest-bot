from aiogram.dispatcher.filters.state import State, StatesGroup


class EditSignatureState(StatesGroup):
    WaitingForSignature = State()
