#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
name = form.getfirst("name")
user = form.getfirst("user")
name = html.escape(name)
user = html.escape(user)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html lang="ru">
        <head>
            <meta charset="utf-8">
            <title>Weather Bot SignIn</title>
        </head>
        <body>""")

print("<h3>Данные на обработку</h3>")
print(f"<p>User's Name: {name}</p>")
print(f"<p>TG Username: {user}</p>")

print("""</body>
        </html>""")
