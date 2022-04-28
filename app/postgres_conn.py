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
    user_name = Column(String())

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def sign_user(self):
        session.add(self)
        session.commit()
        return True


def check_user(user_id):
    s = select(BotUsers).where(BotUsers.user_id == user_id)
    result = session.execute(s).all()
    for item in result:
        for row in item:
            print(row.user_name)
    if len(result) == 1:
        return True, result[0][0].user_name
    else:
        return False, 0


def input_data(user_data):
    user_id, user_name = user_data
    new_user = BotUsers(user_id, user_name)
    return new_user.sign_user()


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)
