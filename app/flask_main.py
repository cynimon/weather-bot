from flask import Flask
from flask import render_template, request
from postgres_conn import input_data


app = Flask(__name__)

head = ("""<!DOCTYPE HTML>
                <html lang="ru">
                <head>
                    <meta charset="utf-8">
                    <title>Weather Bot SignIn</title>
                </head>
                <body>""")

success = ("<h3>Регистрация прошла успешно, можно вернуться к боту</h3>"
           """
            <form action="https://t.me/msc_wnow_bot?start=start">
               <input type="submit" value="Go to Bot" />
           </form>""")

fail = "<h3>Что-то пошло не так, попробуйте в другой раз</h3>"
tail = """</body> </html>"""


def get_user_id(reqt):
    some = str(reqt).split('=')
    return some[1]


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_id = get_user_id(request.environ["HTTP_REFERER"])
        user_name = request.form.get("name")
        result = input_data(user_id, user_name)
        if result:
            return head + success + tail
        else:
            return head + fail + tail
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
