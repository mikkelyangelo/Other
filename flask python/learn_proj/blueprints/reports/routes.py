from flask import Blueprint, render_template, request, flash, redirect,url_for
from sql_provider import SQLProvider
from database import work_with_db, select_dict, call_proc
from blueprints.authorization.access import login_required, auth_required
import json

db_config = json.load(open('configs/config.json'))
report_app = Blueprint('reports', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider('blueprints/reports/sql/')
with open('configs/report.json') as f:
    reports = json.load(f)


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
        find_check_count = provider.get(reports[0]['sql_check'], month=month, year=year)
        check_count = work_with_db(db_config, find_check_count)
        if check_count[0]['count'] == 0:
            # sql = provider.get(reports[0]['sql_create'], month=month, year=year)
            result = call_proc(db_config, 'otchet', year, month)
            print(result)
            if result:
                flash(f"Вы создали отчёт за {month} месяц {year} года", 'success')
                return redirect(url_for('reports.reports_choice'))
            else:
                flash(f"Нельзя создать отчёт на этот месяц и год", 'error')
                return render_template('create_1.html')

        else:
            flash('Такой отчёт уже существует', 'repeat')
            return render_template('create_1.html')


# @report_app.route('/view_1', methods=['GET', 'POST'])
# def view_1():
#     if request.method == 'GET':
#         return render_template('view.html', title=reports[0]['name'])
#         sql = provider.get('view_sql.sql')
#         reports_list = select_dict(db_config, sql)
#         return render_template('view_1.html', reports_list=reports_list)
#     else:
#         month = request.form.get('month')
#         year = request.form.get('year')
#         sql = provider.get_sql('result.sql', month=month, year=year)
#         result = work_with_db(db_config, sql)
#         title = f"Отчёт за {month} месяц {year} года"
#         num = 1
#         return render_template('reports_result.html', result=result, title=title, num=num)

@report_app.route('/view_1', methods=['GET', 'POST'])
def view_1():
    if request.method == 'GET':
        return render_template('view_1.html', title=reports[0]['name'])
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get(reports[0]['sql_check'], month=month, year=year)
        print(find_check_count)
        check_count = select_dict(db_config, find_check_count)
        print(check_count)
        if check_count[0]['count'] != 0:
            sql = provider.get(reports[0]['sql_view'], month=month, year=year)
            result = select_dict(db_config, sql)
            print(result)
            title = f"Количество пациентов у врачей за {month} месяц {year} года"
            return render_template("view_result.html", result=result, title=title, num=1)
        else:
            flash('Такой отчёт ещё не был создан', 'error')
            return render_template('view_1.html', title=reports[0]['name'])