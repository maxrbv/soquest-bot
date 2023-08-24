import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    event_name = Column(String)
    event_date = Column(DateTime, default=datetime.datetime.utcnow)
