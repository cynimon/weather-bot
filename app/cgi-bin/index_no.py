#!/usr/bin/env python3
import cgi
import html
import importlib
app = importlib.import_module('app')

form = cgi.FieldStorage()
userid = form.getfirst("userid")
name = form.getfirst("name")
userid = html.escape(userid)
name = html.escape(name)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html lang="ru">
        <head>
            <meta charset="utf-8">
            <title>Weather Bot SignIn</title>
        </head>
        <body>""")

user_data = (userid, name)
result = app.postgres_conn.input_data(user_data)
if result:
    print("<h3>Регистрация прошла успешно, можно вернуться к боту</h3>")
    print("""
        <form action="https://t.me/msc_wnow_bot">
        <input type="submit" value="Go to Bot" />
    </form>""")
else:
    print("<h3>Что-то пошло не так, попробуйте в другой раз</h3>")
print("""</body>
        </html>""")
