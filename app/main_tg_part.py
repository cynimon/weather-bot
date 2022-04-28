from config import tg_bot_token
import logging
from aiogram import Bot, Dispatcher, executor, types
import weather_api as wa
import postgres_conn as pgc

logging.basicConfig(level=logging.INFO)

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


async def is_user_signed(user_id):
    return pgc.check_user(user_id)


async def checking_data(user_data):
    user_id = user_data["id"]
    # user_id = 22545408
    reply = await is_user_signed(user_id)
    if reply:
        await send_weather(user_id)
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Зарегистрироваться", url="http://0.0.0.0:8000/"))
        await bot.send_message(user_data["id"], f"Необходимо зарегистрироваться в боте\n"
                                                f"Скопируйте в форму свой user_id: {user_data['id']}",
                               reply_markup=keyboard)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Узнать погоду", callback_data="click_weather"))
    await message.answer("Привет! Это бот, который присылает тебе погоду в Москве", reply_markup=keyboard)


async def send_weather(chat_id):
    reply = wa.get_weather()
    await bot.send_message(chat_id, reply)


@dp.callback_query_handler(text="click_weather")
async def send_random_value(call: types.CallbackQuery):
    user_data = call.__getitem__('from')
    await call.answer()
    await checking_data(user_data)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
