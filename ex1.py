# Задание
# 📌 Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# 📌 При отправке которой будет создан cookie файл с данными
# пользователя
# 📌 Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# 📌 На странице приветствия должна быть кнопка "Выйти"
# 📌 При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return f'Привет {name}!'


@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    # email = request.form.get('email')
    # return f'Hello, {name} ({email})!'
    return redirect(url_for('hello', name = name))
    return render_template('form.html')

if __name__ == '__main__':
    app.run()