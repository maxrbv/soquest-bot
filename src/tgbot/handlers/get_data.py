from aiogram.types import ChatType, CallbackQuery, InputFile

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from tgbot.messages.messages import GET_DATA_FAIL_MESSAGE, GET_DATA_SUCCESS_MESSAGE, GET_DATA_FAIL_FILE_MESSAGE
from tgbot.models.users import User
from tgbot.models.events import Event
from tgbot.models.users import Base as Userbase
from tgbot.models.events import Base as EventBase
from parser.soquest import SoQuest

from config import dp, bot
from settings import DB_URL


engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Userbase.metadata.create_all(engine)
EventBase.metadata.create_all(engine)


@dp.callback_query_handler(
    lambda query: query.data == 'btn_get_data',
    chat_type=ChatType.PRIVATE
)
async def get_data_callback(query: CallbackQuery):
    await query.answer()

    user_id = query.from_user.id

    session = Session()
    user = session.query(User).filter_by(user_id=user_id).first()

    event_name = 'get data'
    event = Event(
        user_id=user_id,
        event_name=event_name
    )

    session.add(event)
    session.commit()

    if not user.address or not user.signature:
        await query.message.answer(GET_DATA_FAIL_MESSAGE)
    else:
        form_doc_message = await query.message.answer(GET_DATA_SUCCESS_MESSAGE)
        soquest = SoQuest(user_id=user_id, address=user.address, signature=user.signature)
        filename = await soquest.parse_data()

        if filename:
            await form_doc_message.delete()
            with open(filename, "rb") as f:
                document = InputFile(f)
                await query.message.answer_document(document, caption="Ваш готовый файл")
        else:
            await query.message.answer(GET_DATA_FAIL_FILE_MESSAGE)
