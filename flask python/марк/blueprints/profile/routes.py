from flask import Blueprint, render_template, request, session
from sql_provider import SQLProvider
from database import work_with_db
from blueprints.authorization.access import login_required
import json


db_config = json.load(open('configs/config.json'))
profile_app = Blueprint('profile', __name__, template_folder='templates')
provider = SQLProvider('blueprints/profile/sql/')


@profile_app.route('/')
@login_required
def index():
    return render_template('profile-index.html',user=session.get('group_name'))


@profile_app.route('/prov1', methods=['GET', 'POST'])
@login_required
def get_sql1():
    if request.method == 'GET':
        return render_template('prov1.html')
    else:
        cost_to = request.form.get('cost_to', None)
        if cost_to is not None:
            sql = provider.get('task1.sql', cost_to=cost_to)
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
        if date_end is not None and date_end is not None:
            sql = provider.get('task2.sql', date_start=date_start, date_end=date_end)
            result = work_with_db(db_config, sql)
            if not result:
                return 'not found'
            return render_template('output2.html', str=result)


