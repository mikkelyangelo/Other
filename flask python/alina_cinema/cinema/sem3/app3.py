import json
from flask import Flask, render_template, session
from blueprint_query.route import blueprint_query
from blueprint_auth.auth import blueprint_auth
from entry.routes import entry_app
from reports.routes import report_app

app = Flask(__name__)
with open('../db_config.json') as f:
    app.config['db_config'] = json.load(f)

with open('../access.json') as f:
    app.config['access_config'] = json.load(f)

with open('../rep.json') as f:
    app.config['rep_config'] = json.load(f)

app.register_blueprint(blueprint_query, url_prefix='/query')
app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(report_app, url_prefix='/report')
app.register_blueprint(entry_app, url_prefix='/entry')
app.secret_key = "You will never guess"


@app.route('/')
def main_menu():
    # session['user_id'] = 1
    # session['user_group'] = 'manager'

    return render_template('main_menu.html')


@app.route('/exit')
def exit_fuc():
    session.clear()
    return "До свидания, хотите, заходите ещё.\n Нет? Так нет."



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
