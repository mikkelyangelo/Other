import json
from flask import Flask, render_template, session
from bp_auth.route import bp_auth
from bp_queries.route import bp_queries
from bp_reports.route import bp_reports
from sql_provider import SQL_Provider


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DB_CONFIG'] = json.load(open('configs/db_config.json'))
app.config['ACCESS_CONFIG'] = json.load(open('configs/access.json'))

app.register_blueprint(bp_queries, url_prefix='/search')
app.register_blueprint(bp_auth, url_prefix='/auth')
app.register_blueprint(bp_reports, url_prefix='/reports')

with open('configs/db_config.json') as f:
    app.config['db_config'] = json.load(f)
provider = SQL_Provider('sql/')


@app.route('/')
def home_page():
    if 'login' in session:
        return render_template('main.html', if_logged=1)
    return render_template('main.html', if_logged=0)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5001, debug = True)


