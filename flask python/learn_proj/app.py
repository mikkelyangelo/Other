# стандартные пакеты (которые не нужно скачивать извне)
import json

# стандартные пакеты (которые нужно дополнительно устанавливать)

from flask import Flask, render_template, session, flash, redirect, url_for

from blueprints.authorization.access import login_required
# модули проекта (которые пишем сами)
from blueprints.profile.routes import profile_app
from blueprints.authorization.routes import auth_app
from blueprints.reports.routes import report_app
from blueprints.entry.routes import entry_app
from sql_provider import SQLProvider
from database import get_db_config

app = Flask(__name__)
db_config = json.load(open('configs/config.json'))

app.register_blueprint(profile_app, url_prefix='/profile')
app.register_blueprint(auth_app, url_prefix='/authorization')
app.register_blueprint(report_app, url_prefix='/reports')
app.register_blueprint(entry_app, url_prefix='/entry')

provider = SQLProvider('blueprints/profile/sql/')
app.config['SECRET_KEY'] = 'super secret key'
app.config['DB_CONFIG'] = get_db_config()


@app.route('/')
def i():
    return render_template('mm.html')


@app.route('/second')
@login_required
def index():
    return render_template('menu.html', group=session['group_name'], log_status=1)


@app.route('/session-clear')  # ? Очистка сессии.
def clear_session():
    session.clear()
    return ''


@app.route('/exit')
def exit_handler():
    session.clear()
    return render_template('mm.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7002)
