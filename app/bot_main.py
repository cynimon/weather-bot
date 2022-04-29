import logging
from aiogram import Bot, Dispatcher, executor, types
import weather_api as wa
import database_part as pgc
from dotenv import load_dotenv
import os

load_dotenv()

tg_bot_token = os.getenv("tg_bot_token")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


async def checking_data(user_data):
    user_id = user_data["id"]
    reply, username = await pgc.is_user_signed(user_id)
    if reply:
        await send_weather(user_id, username)
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Вперёд  \U000027a1", url=f"http://127.0.0.1:5000?uid={user_id}"))
        await bot.send_message(user_data["id"], f"Необходимо зарегистрироваться в боте\n", reply_markup=keyboard)


async def send_weather(chat_id, user_name):
    reply = f"{user_name}, только для тебя, погода в Москве:\n" + wa.get_weather()
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Обновить", callback_data="click_weather"))
    await bot.send_message(chat_id, reply, reply_markup=keyboard)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Узнать погоду", callback_data="click_weather"))
    await message.answer("Привет! Это бот, который присылает тебе погоду в Москве", reply_markup=keyboard)


@dp.callback_query_handler(text="click_weather")
async def send_welcome(call: types.CallbackQuery):
    user_data = call.__getitem__('from')
    await call.answer()
    await checking_data(user_data)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
