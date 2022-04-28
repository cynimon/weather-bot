from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

db_config = "postgresql://postgres:11qa@localhost:5432/weather_bot"

db = create_engine(db_config)
base = declarative_base()


class BotUsers(base):
    __tablename__ = 'bot_users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), unique=True)
    name = Column(String())
    username = Column(String())

    def __init__(self, user_id, name, username):
        self.user_id = user_id
        self.name = name
        self.username = username

    def sign_user(self):
        session.add(self)
        session.commit()
        return True


def check_user(user_id):
    s = select(BotUsers).where(BotUsers.user_id == user_id)
    result = len(session.execute(s).all())
    if result == 1:
        return True
    else:
        return False

def input_data(user_data):
    pass

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)
