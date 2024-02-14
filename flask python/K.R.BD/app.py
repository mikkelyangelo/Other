import json
from blueprints.blueprint_query.route import blueprint_query
from flask import Flask, render_template, session
from blueprints.blueprint_auth.auth import blueprint_auth
from blueprints.edit.routes import edit_app
from blueprints.reports.routes import report_app

app = Flask(__name__)
with open('config/db_config.json') as f:
    app.config['db_config'] = json.load(f)


app.register_blueprint(blueprint_query, url_prefix='/query')
app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(edit_app, url_prefix='/edit')
app.register_blueprint(report_app, url_prefix='/reports')
app.secret_key = "You will never guess"


@app.route('/')
def start_menu():
    return render_template('start_menu.html')

@app.route('/main')
def main_menu():
    return render_template('main_menu1.html')

@app.route('/exit')
def exit_ses():
    session.clear()
    return render_template('start_menu.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)