from flask import Blueprint, render_template, request
from sql_provider import SQLProvider
from database import work_with_db
from blueprints.authorization.access import login_required, auth_required
import json


db_config = json.load(open('configs/config.json'))
profile_app = Blueprint('profile', __name__, template_folder='templates')
provider = SQLProvider('blueprints/profile/sql/')


@profile_app.route('/')
@auth_required
@login_required

def index():
    return render_template('profile-index.html')


@profile_app.route('/prov1', methods=['GET', 'POST'])
@login_required
def get_sql1():
    if request.method == 'GET':
        return render_template('prov1.html')
    else:
        year = request.form.get('year', None)
        month = request.form.get('month', None)
        if year is not None:
            sql = provider.get('task1.sql', year=year, month=month)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output.html', str=result)


@profile_app.route('/prov2', methods=['GET', 'POST'])
@login_required
def get_sql2():
    if request.method == 'GET':
        return render_template('prov2.html')
    else:
        date_start = request.form.get('date_start', None)
        date_end = request.form.get('date_end', None)
        if date_start is not None and date_end is not None:
            sql = provider.get('task2.sql', date_start=date_start, date_end=date_end)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output2.html', result=result)


@profile_app.route('/prov3', methods=['GET', 'POST'])
@login_required
def get_sql3():
    if request.method == 'GET':
        return render_template('prov3.html')
    else:
        title = request.form.get('title', None)
        if title is not None:
            sql = provider.get('task3.sql', title=title)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output3.html', str=result)

