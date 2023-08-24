from aiogram.types import Message, ChatType

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from tgbot.messages.messages import START_MESSAGE
from tgbot.menus.main_menu import mainMenu
from tgbot.models.users import User, Base

from config import dp, bot
from settings import DB_URL


engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


@dp.message_handler(
    commands=['start'],
    chat_type=ChatType.PRIVATE
)
async def start(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.username

    session = Session()
    user = session.query(User).filter_by(user_id=user_id).first()

    if user is None:
        user = User(user_id=user_id, user_name=user_name)
        session.add(user)
        session.commit()

    await bot.send_message(
        chat_id=message.from_user.id,
        text=START_MESSAGE,
        parse_mode='MarkdownV2',
        reply_markup=mainMenu
    )
