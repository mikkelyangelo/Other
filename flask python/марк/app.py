# стандартные пакеты (которые не нужно скачивать извне)
import json

# стандартные пакеты (которые нужно дополнительно устанавливать)

from flask import Flask, render_template, session

# модули проекта (которые пишем сами)
from blueprints.edit.routes import edit_app
from blueprints.profile.routes import profile_app
from blueprints.authorization.routes import auth_app
from sql_provider import SQLProvider
from database import get_db_config

app = Flask(__name__)
db_config = json.load(open('configs/config.json'))

app.register_blueprint(profile_app, url_prefix='/profile')
app.register_blueprint(auth_app, url_prefix='/authorization')
app.register_blueprint(edit_app, url_prefix='/edit')

provider = SQLProvider('blueprints/profile/sql/')
app.config['SECRET_KEY'] = 'super secret key'
app.config['DB_CONFIG'] = get_db_config()


@app.route('/')
def index():
    return render_template('menu.html')


@app.route('/counter')  # ? Счётчик посещений сайта.
def count_visits():
    counter = session.get('count', None)
    if counter is None:
        session['count'] = 0
    else:
        session['count'] = session['count'] + 1
    return f"Your count: {session['count']}"


@app.route('/session-clear')  # ? Очистка сессии.
def clear_session():
    session.clear()
    return ''


@app.route('/exit')
def exit_handler():
    session.clear()
    return 'До свидания! Заходите ещё!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8005)
