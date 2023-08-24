from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from settings import TG_TOKEN


bot = Bot(token=TG_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
