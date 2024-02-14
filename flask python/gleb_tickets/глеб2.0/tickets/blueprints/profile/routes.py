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
        days = request.form.get('days', None)
        if days is not None:
            sql = provider.get('task2.sql', days=days)
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

@profile_app.route('/prov4', methods=['GET', 'POST'])
def get_sql4():
    if request.method == 'GET':
        return render_template('prov4.html')
    else:
        year = request.form.get('year', None)
        if year is not None:
            sql = provider.get('task4.sql', year=year)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output4.html', str=result)