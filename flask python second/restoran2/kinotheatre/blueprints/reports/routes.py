from flask import Blueprint, render_template, request, flash, redirect,url_for
from sql_provider import SQLProvider
from database import work_with_db, select_dict
from blueprints.authorization.access import login_required, auth_required
import json

db_config = json.load(open('configs/config.json'))
report_app = Blueprint('reports', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider('blueprints/reports/sql/')
with open('configs/report.json', 'r', encoding='utf-8') as f:
    reports = json.load(f)


@report_app.route('/')
@auth_required
@login_required
def reports_choice():
    return render_template('report_choice.html', reports=reports)

@report_app.route('/tickets')
@auth_required
@login_required
def tickets_create():
    return render_template('create_tickets.html', reports=reports)

@report_app.route('/create_1', methods=['GET', 'POST'])
@login_required
def create_1():
    if request.method == 'GET':
        return render_template('create_1.html')
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get(reports[0]['sql_check'], month=month, year=year)
        check_count = work_with_db(db_config, find_check_count)
        if check_count[0]['count'] == 0:
            sql = provider.get(reports[0]['sql_create'], month=month, year=year)
            result = select_dict(db_config, sql)
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
@login_required
def view_1():
    if request.method == 'GET':
        return render_template('view_1.html', title=reports[0]['name'])
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get(reports[0]['sql_check'], month=month, year=year)
        check_count = select_dict(db_config, find_check_count)
        if check_count[0]['count'] != 0:
            sql = provider.get(reports[0]['sql_view'], month=month, year=year)
            result = select_dict(db_config, sql)
            title = f"Отчёт за {month} месяц {year} года"
            return render_template("view_result.html", result=result, title=title, num=1)
        else:
            flash('Такой отчёт ещё не был создан', 'error')
            return render_template('view_1.html')



@report_app.route('/create_2', methods=['GET', 'POST'])
@login_required
def create_2():
    if request.method == 'GET':
        return render_template('create_2.html')
    else:
        seans_num = request.form.get('seans_num')
        find_check_count = provider.get(reports[1]['sql_check'],seans_num=seans_num)
        check_count = work_with_db(db_config, find_check_count)
        if check_count[0]['count'] == 0:
            sql = provider.get(reports[1]['sql_create'], seans_num=seans_num)
            result = select_dict(db_config, sql)
            if result is None:
                # flash(f"Вы создали отчёт за {month} месяц {year} года", 'success')
                return redirect(url_for('reports.tickets_create'))
            else:
                flash(f"Нельзя создать отчёт на этот месяц и год", 'error')
                return render_template('create_2.html')
        else:
            flash('Такой отчёт уже существует', 'error')
            return render_template('create_2.html')

@report_app.route('/view_2', methods=['GET', 'POST'])
@login_required
def view_2():
    if request.method == 'GET':
        return render_template('view_2.html', title=reports[1]['name'])
    else:
        seans_num = request.form.get('seans_num')
        find_check_count = provider.get(reports[1]['sql_check'], seans_num=seans_num)
        check_count = select_dict(db_config, find_check_count)
        if check_count[0]['count'] != 0:
            sql = provider.get(reports[1]['sql_view'], seans_num=seans_num)
            result = select_dict(db_config, sql)
            title = f"Отчёт на {seans_num} сеанс"
            return render_template("view_result2.html", result=result, title=title, num=1)
        else:
            flash('Такой отчёт ещё не был создан', 'error')
            return render_template('view_2.html')

@report_app.route('/create_3', methods=['GET', 'POST'])
@login_required
def create_3():
    if request.method == 'GET':
        return render_template('create_3.html')
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get(reports[2]['sql_check'], month=month, year=year)
        print(find_check_count)
        check_count = work_with_db(db_config, find_check_count)
        if check_count[0]['count'] == 0:
            sql = provider.get(reports[2]['sql_create'], month=month, year=year)
            result = select_dict(db_config, sql)
            if result is None:
                flash(f"Вы создали отчёт за {month} месяц {year} года", 'success')
                return redirect(url_for('reports.reports_choice'))
            else:
                flash(f"Нельзя создать отчёт на этот месяц и год", 'error')
                return render_template('create_3.html')

        else:
            flash('Такой отчёт уже существует', 'error')
            return render_template('create_3.html')

@report_app.route('/view_3', methods=['GET', 'POST'])
@login_required
def view_3():
    if request.method == 'GET':
        return render_template('view_3.html', title=reports[0]['name'])
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get(reports[2]['sql_check'], month=month, year=year)
        check_count = select_dict(db_config, find_check_count)
        if check_count[0]['count'] != 0:
            sql = provider.get(reports[2]['sql_view'], month=month, year=year)
            result = select_dict(db_config, sql)
            title = f"Отчёт за {month} месяц {year} года"
            return render_template("view_result3.html", result=result, title=title, num=1)
        else:
            flash('Такой отчёт ещё не был создан', 'error')
            return render_template('view_3.html')
