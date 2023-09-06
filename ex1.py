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

from flask import Flask, request, render_template, redirect, url_for, make_response, session

app = Flask(__name__)

app.secret_key = ''
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/hello/<name>')
# def hello(name):
#     return f'Привет {name}!'
#
#
# @app.get('/submit')
# def submit_get():
#     return render_template('form.html')
#
#
# @app.post('/submit')
# def submit_post():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     # return f'Hello, {name} ({email})!'
#     response = make_response("Cookie установлен")
#     response.set_cookie(name, email)
#     return response
#     return redirect(url_for('hello', name = name))
#     # return response
#     return render_template('form.html')
#
@app.route('/log/', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('log.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()