from report.utils import report_required, query_execution
from flask import (Blueprint, render_template, session,
                   current_app, request, flash)

from database.sql_provider import SQLProvider
from database.operations import call_proc

from decorators.routes import login_required, role_required


reports_app = Blueprint('reports_app', __name__, template_folder='templates')
sql_provider = SQLProvider('report/sql')


@reports_app.route('/')
@login_required(session)
@role_required(session)
def reports_index():
    return render_template('reports_index.html',
                           reports=current_app.config['reports_list'])


@reports_app.route('/view-report', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
@report_required
def view_report(report):
    if request.method == 'POST':
        check_flag, result = query_execution(
            'date', report['sql_statement'], sql_provider)
        if check_flag:
            if report['rep_id'] == 1:
                cost = sum(item['count'] for item in result)
                return render_template('view_report.html',
                                       name=report['rep_name'],
                                       rep_id=report['rep_id'],
                                       result=result,
                                       cost=cost)
            else:
                return render_template('view_report2.html',
                                       name=report['rep_name'],
                                       rep_id=report['rep_id'],
                                       result=result)

        else:
            flash(result, 'error')
    return render_template('view_report.html',
                           name=report['rep_name'],
                           rep_id=report['rep_id'])


@reports_app.route('/create-report', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
@report_required
def create_report(report):
    if request.method == 'POST':
        procedure = report['procedure']
        if not procedure:
            flash('Процедура не найдена', 'error')
            return render_template('create_report.html',
                                   name=report['rep_name'],
                                   rep_id=report['rep_id'])
        date = request.form.get('date')

        result = call_proc(
            current_app.config['MYSQL_DB_CONFIG'], procedure, f'{date}-01')

        if result:
            flash(result, 'error')
        else:
            flash('Отчет успешно создан', 'okay')
    return render_template('create_report.html',
                           name=report['rep_name'],
                           rep_id=report['rep_id'])
