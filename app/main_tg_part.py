from config import tg_bot_token, weather_token
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests as r
import datetime as dt

logging.basicConfig(level=logging.INFO)

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


def get_weather(weather_token):
    req = r.get(
        f"https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid={weather_token}&units=metric"
    )
    data = req.json()

    cur_weather = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    sunrise_time = dt.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_time = dt.datetime.fromtimestamp(data["sys"]["sunset"])

    weather = (f"~~~{dt.datetime.now().strftime('%d-%m-%Y %H:%M')}~~~\n"
          f"Погода в Москве:\nТемпература: {cur_weather} C°\nВлажность: {humidity}%\nДавление: {pressure} мм.рт.мт\n"
          f"Скорость ветра: {wind} м/с\nРассвет: {sunrise_time}\nЗакат: {sunset_time}\nХорошего дня!")
    return weather


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Это бот, который присылает тебе погоду в Москве")


@dp.message_handler(commands=['weather'])
async def send_weather(message: types.Message):
    reply = get_weather(weather_token)
    await message.reply(reply)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
