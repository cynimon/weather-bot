from sqlalchemy import create_engine
from sqlalchemy import Column, String, BigInteger, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

db_config = "postgresql://postgres:postgres@localhost:5432/postgres"

db = create_engine(db_config)
base = declarative_base()


# модель данных пользователей бота
class BotUsers(base):
    __tablename__ = 'bot_users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger(), unique=True)
    user_name = Column(String())

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def sign_user(self):
        session.add(self)
        session.commit()
        return True


# проверка, зарегистрирован ли пользователь в боте и передача его имени в бота
async def is_user_signed(user_id):
    s = select(BotUsers).where(BotUsers.user_id == user_id)
    result = session.execute(s).all()
    if len(result) == 1:
        return True, result[0][0].user_name
    else:
        return False, 0


# регистрация пользователя в боте
def input_data(user_id, user_name):
    new_user = BotUsers(user_id, user_name)
    return new_user.sign_user()


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)
