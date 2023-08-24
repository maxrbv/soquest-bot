from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ChatType, CallbackQuery

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from tgbot.states.edit_address import EditAddressState
from tgbot.messages.messages import EDIT_ADDRESS_MESSAGE, EDIT_ADDRESS_SUCCESS_MESSAGE, EDIT_ADDRESS_FAIL_MESSAGE
from tgbot.models.users import User
from tgbot.models.events import Event
from tgbot.models.users import Base as Userbase
from tgbot.models.events import Base as EventBase

from config import dp
from settings import DB_URL


engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Userbase.metadata.create_all(engine)
EventBase.metadata.create_all(engine)


@dp.callback_query_handler(
    lambda query: query.data == 'btn_edit_address',
    chat_type=ChatType.PRIVATE
)
async def edit_address_callback(query: CallbackQuery):
    await query.answer()

    user_id = query.from_user.id
    event_name = "address change"

    session = Session()

    event = Event(
        user_id=user_id,
        event_name=event_name
    )

    session.add(event)
    session.commit()

    await EditAddressState.WaitingForAddress.set()
    await query.message.answer(EDIT_ADDRESS_MESSAGE)


@dp.message_handler(
    state=EditAddressState.WaitingForAddress,
    chat_type=ChatType.PRIVATE
)
async def process_address(message: Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['address'] = message.text.strip()

    session = Session()
    user = session.query(User).filter_by(user_id=user_id).first()
    if user:
        user.update_address(session, data['address'])
        await message.answer(EDIT_ADDRESS_SUCCESS_MESSAGE)
    else:
        await message.answer(EDIT_ADDRESS_FAIL_MESSAGE)

    await state.finish()
