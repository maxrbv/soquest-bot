from aiogram.types import ChatType, CallbackQuery, InputFile

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from tgbot.messages.messages import GET_DAILY_FAIL_MESSAGE
from tgbot.models.users import User
from tgbot.models.events import Event
from tgbot.models.users import Base as Userbase
from tgbot.models.events import Base as EventBase
from parser.soquest import SoQuest

from config import dp
from settings import DB_URL


GET_DAILY_MAPPER = {
    '0': 'Вы уже получали сегодня гемы',
    '1': 'Гемы успешно получены',
    '2': 'Неверный адрес или подпись',
    '404': 'Ошибка с запросом. Повторите снова или напишите @UrwaLeason'
}


engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Userbase.metadata.create_all(engine)
EventBase.metadata.create_all(engine)


@dp.callback_query_handler(
    lambda query: query.data == 'btn_get_daily',
    chat_type=ChatType.PRIVATE
)
async def get_data_callback(query: CallbackQuery):
    await query.answer()

    user_id = query.from_user.id

    session = Session()
    user = session.query(User).filter_by(user_id=user_id).first()

    event_name = 'get daily'
    event = Event(
        user_id=user_id,
        event_name=event_name
    )

    session.add(event)
    session.commit()

    if not user.address or not user.signature:
        await query.message.answer(GET_DAILY_FAIL_MESSAGE)
    else:
        soquest = SoQuest(user_id=user_id, address=user.address, signature=user.signature)
        req_answer = await soquest.collect_daily()
        try:
            req_mapper = GET_DAILY_MAPPER[req_answer]
        except:
            req_mapper = 'Произошла непредвиденная ошибка. Ответ на ваш запрос: ' + req_answer
        await query.message.answer(req_mapper)
