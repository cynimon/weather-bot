from flask import Flask
from flask import abort, render_template, request
import werkzeug.exceptions
from database_part import input_data

app = Flask(__name__)

# Страница после успешной регистрации нового пользователя
success_answer = ("""<!DOCTYPE HTML>
                <html lang="ru">
                <head>
                    <meta charset="utf-8">
                    <title>Weather Bot SignIn</title>
                </head>
                <body>
                <h3>Регистрация прошла успешно, можно вернуться к боту</h3>
                <form action="https://t.me/msc_wnow_bot?start=start">
                <input type="submit" value="Go to Bot"/></form>
                </body> 
                </html>""")


# Получение айди юзера из get-запроса при переходе из telegram
def get_user_id(reqt):
    some = str(reqt).split('=')
    return some[1]


# воспроизведение ошибки при некорректном имени пользователя
def name_valid(username):
    if username.isalnum():
        return username
    else:
        abort(400)


# обработка ошибки сервера (500 код)
@app.errorhandler(werkzeug.exceptions.InternalServerError)
def hande_not_found(e):
    return "<h3>Что-то пошло не так, попробуйте в другой раз</h3>\n" \
           "<h4>Возможно, ваш аккаунт уже зарегистрирован - перезапустите бота</h4>", 500


# обработка искусственной ошибки ввода данных (400 код)
@app.errorhandler(werkzeug.exceptions.BadRequest)
def hande_not_found(e):
    return "<h3>Что-то пошло не так, попробуйте в другой раз</h3>\n" \
           "<h4>Возможно, ваше имя введено некорректно - в нём должны быть только буквы или цифры</h4>", 400


# получение данных пользователя и регистрация
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_name = name_valid(request.form.get("name"))
        user_id = get_user_id(request.environ["HTTP_REFERER"])
        result = input_data(user_id, user_name)
        if result:
            return success_answer
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
