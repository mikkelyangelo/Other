from typing import Tuple, Any
from flask import (
    Blueprint,
    render_template,
    request,
    current_app,
    flash,
    session
)

from database.sql_provider import SQLProvider
from database.operations import select_from_db, insert_into_db

from decorators.routes import login_required, role_required

queries_app: Blueprint = Blueprint(
    'queries_app', __name__, template_folder='templates')
sql_provider: SQLProvider = SQLProvider('queries/sql')


@queries_app.route('/')
@login_required(session)
@role_required(session)
def queries_index():
    """
    Обрабатывает главную страницу запросов.
    """
    return render_template('queries_index.html', role=session['role'])


def query_execution(key, sql_statement_name):
    """
    Выполняет SQL-запрос и возвращает результат.
    """
    data = request.form.get(key)

    if not data:
        return False, "Данные не введены"

    sql_statement = sql_provider.get(sql_statement_name, {key: data})
    result = select_from_db(
        current_app.config['MYSQL_DB_CONFIG'], sql_statement)

    if not result:
        return False, "Нет результатов"

    return True, result


@queries_app.route('/search-by-city', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def search_candidate_by_city():
    if request.method == 'GET':
        return render_template('search_candidate_by_city.html')
    else:
        check_flag, result = query_execution(
            'city', 'search_candidate_by_city.sql')

        if check_flag:
            return render_template('search_candidate_by_city.html', result=result)
        else:
            flash(result, 'error')
            return render_template('search_candidate_by_city.html', message=result)


@queries_app.route('/search-vacancy', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def show_vacancy():
    if request.method == 'GET':
        return render_template('search_vacancy.html')
    else:
        check_flag, result = query_execution(
            'vacancy', 'search_vacancy.sql')

        if check_flag:
            return render_template('search_vacancy.html', result=result)
        else:
            flash(result, 'error')
            return render_template('search_vacancy.html', message=result)


@queries_app.route('/show-employees', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def show_employees():
    if request.method == 'GET':
        return render_template('search_emp_by_name.html')
    else:
        check_flag, result = query_execution(
            'name', 'search_emp_by_name.sql')

        if check_flag:
            return render_template('search_emp_by_name.html', result=result)
        else:
            flash(result, 'error')
            return render_template('search_emp_by_name.html', message=result)


@queries_app.route('/show-interviews', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def show_interviews():
    if request.method == 'GET':
        return render_template('show_interviews.html')
    else:
        check_flag, result = query_execution(
            'date', 'show_interviews.sql')

        if check_flag:
            return render_template('show_interviews.html', result=result)
        else:
            flash(result, 'error')
            return render_template('show_interviews.html', message=result)
