import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    user_name = Column(String)
    address = Column(String, default='')
    signature = Column(String, default='')
    reg_date = Column(DateTime, default=datetime.datetime.utcnow)

    def update_address(self, session: Session, new_address: str):
        self.address = new_address
        session.commit()

    def update_signature(self, session: Session, new_signature: str):
        self.signature = new_signature
        session.commit()
