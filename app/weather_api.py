from config import weather_token
import requests as r
import datetime as dt


def get_weather():
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
               f"Температура: {cur_weather} C°\nВлажность: {humidity}%\nДавление: {pressure} мм.рт.мт\n"
               f"Скорость ветра: {wind} м/с\nРассвет: {sunrise_time}\nЗакат: {sunset_time}\nХорошего дня!")
    return weather
