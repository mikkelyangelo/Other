from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
from db_connect import select_dict
from sql_provider import SQL_Provider
import access
import json


bp_reports = Blueprint('bp_reports', __name__, template_folder='templates', static_folder='static')
provider = SQL_Provider('bp_reports/sql')
with open('configs/reports.json') as f:
    reports = json.load(f)


@bp_reports.route('/')
@access.auth_required
@access.group_required
def choice():
    if request.method == 'GET':
        return render_template('reports_choice.html', reports=reports)

@bp_reports.route('/create_1', methods=['GET', 'POST'])
@access.group_required
def create_1():
    if request.method == 'GET':
        return render_template('create.html', title=reports[0]['n   ame'])
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get_sql(reports[0]['sql_check'], month=month, year=year)
        check_count = select_dict(current_app.config['DB_CONFIG'], find_check_count)
        if check_count[0]['count'] == 0:
            sql = provider.get_sql(reports[0]['sql_create'], month=month, year=year)
            result = select_dict(current_app.config['DB_CONFIG'], sql)
            if result is None:
                flash(f"Вы создали отчёт за {month} месяц {year} года", 'success')
                return redirect(url_for('bp_reports.choice'))
            else:
                flash(f"Нельзя создать отчёт на этот месяц и год", 'error')
                return render_template('create.html', title=reports[0]['name'])

        else:
            flash('Такой отчёт уже существует', 'error')
            return render_template('create.html', title=reports[0]['name'])

@bp_reports.route('/create_2', methods=['GET', 'POST'])
@access.group_required
def create_2():
    if request.method == 'GET':
        return render_template('create.html', title=reports[1]['name'])
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get_sql(reports[1]['sql_check'], month=month, year=year)
        check_count = select_dict(current_app.config['DB_CONFIG'], find_check_count)
        if check_count[0]['count'] == 0:
            sql = provider.get_sql(reports[1]['sql_create'], month=month, year=year)
            result = select_dict(current_app.config['DB_CONFIG'], sql)
            if result is None:
                flash(f"Вы создали отчёт за {month} месяц {year} года", 'success')
                return redirect(url_for('bp_reports.choice'))
            else:
                flash(f"Нельзя создать отчёт на этот месяц и год", 'error')
                return render_template('create.html', title=reports[1]['name'])

        else:
            flash('Такой отчёт уже существует', 'error')
            return render_template('create.html', title=reports[1]['name'])

@bp_reports.route('/view_1', methods=['GET', 'POST'])
@access.group_required
def view_1():
    if request.method == 'GET':
        return render_template('view.html', title=reports[0]['name'])
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get_sql(reports[0]['sql_check'], month=month, year=year)
        check_count = select_dict(current_app.config['DB_CONFIG'], find_check_count)
        if check_count[0]['count'] != 0:
            sql = provider.get_sql(reports[0]['sql_view'], month=month, year=year)
            result = select_dict(current_app.config['DB_CONFIG'], sql)
            title = f"Количество пациентов у врачей за {month} месяц {year} года"
            return render_template("view_result_1.html", result=result, title=title, num=1)
        else:
            flash('Такой отчёт ещё не был создан', 'error')
            return render_template('view.html')

@bp_reports.route('/view', methods=['GET', 'POST'])
@access.group_required
def view_2():
    if request.method == 'GET':
        return render_template('view.html', title=reports[1]['name'])
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        find_check_count = provider.get_sql(reports[1]['sql_check'], month=month, year=year)
        check_count = select_dict(current_app.config['DB_CONFIG'], find_check_count)
        if check_count[0]['count'] != 0:
            sql = provider.get_sql(reports[1]['sql_view'], month=month, year=year)
            result = select_dict(current_app.config['DB_CONFIG'], sql)
            title = f"Пациенты, пришедшие на приём за {month} месяц {year} года"
            return render_template("view_result_2.html", result=result, title=title, num=2)
        else:
            flash('Такой отчёт ещё не был создан', 'error')
            return render_template('view.html', title=reports[1]['name'])