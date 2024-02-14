from flask import Blueprint, render_template, request, flash, redirect,url_for
from sql_provider import SQLProvider
from database import work_with_db
from blueprints.authorization.access import login_required, auth_required
import json

db_config = json.load(open('configs/config.json'))
report_app = Blueprint('reports', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider('blueprints/reports/sql/')

reports = [{'id': 1, 'name': 'Отчёт'}]


@report_app.route('/')
def reports_choice():
    return render_template('report_choice.html', reports=reports)

@report_app.route('/create_1', methods=['GET', 'POST'])
def create_1():
    if request.method == 'GET':
        return render_template('create_1.html')
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get('sql2.sql', month=month, year=year)
        check_count = work_with_db(db_config, find_check_count)
        if check_count[0]['count'] == 0:
            sql = provider.get('sql1.sql', month=month, year=year)
            result = work_with_db(db_config, sql)
            if result is None:
                flash(f"Вы создали отчёт за {month} месяц {year} года", 'success')
                return redirect(url_for('reports.reports_choice'))
            else:
                flash(f"Нельзя создать отчёт на этот месяц и год", 'error')
                return render_template('create_1.html')

        else:
            flash('Такой отчёт уже существует', 'error')
            return render_template('create_1.html')


@report_app.route('/view_1', methods=['GET', 'POST'])
def view_1():
    if request.method == 'GET':
        sql = provider.get('view_sql.sql')
        reports_list = work_with_db(db_config, sql)
        return render_template('view_1.html', reports_list=reports_list)
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        sql = provider.get_sql('result.sql', month=month, year=year)
        result = work_with_db(db_config, sql)
        title = f"Отчёт за {month} месяц {year} года"
        num = 1
        return render_template('reports_result.html', result=result, title=title, num=num)
