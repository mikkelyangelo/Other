from flask import (Blueprint, render_template, request,
                   current_app, flash, session, redirect, url_for)
from database.sql_provider import SQLProvider
from database.operations import select_from_db, insert_into_db
from database.connection import DBContextManager

from decorators.routes import login_required, role_required

from datetime import date

basket_app = Blueprint('basket_app', __name__, template_folder='templates')
sql_provider = SQLProvider('basket/sql')


@basket_app.route('/', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def get_vacancies():
    if request.method == 'GET':
        sql_statement = sql_provider.get('get_vacancies.sql', {})
        result = select_from_db(
            current_app.config['MYSQL_DB_CONFIG'], sql_statement)

        return render_template('show_vacancies.html', vacancies=result)

    if request.method == 'POST':
        vacancy_id = request.form['vacancy_id']
        username = session['user']

        sql_statement = sql_provider.get('check_currents_responses.sql', {
            'username': username,
        })

        result_for_check = select_from_db(
            current_app.config['MYSQL_DB_CONFIG'], sql_statement)

        for id in result_for_check:
            if int(id['vacancy_id']) == int(vacancy_id):
                flash('Уже есть отклик на эту вакансию', 'error')
                return redirect(url_for('basket_app.get_vacancies'))

        sql_statement = sql_provider.get('add_vacancy_in_list.sql', {
            'vacancy_id': vacancy_id,
            'username': username
        })

        insert_into_db(current_app.config['MYSQL_DB_CONFIG'], sql_statement)
        flash('Отклик отправлен', 'okay')

        return redirect(url_for('basket_app.get_vacancies'))


@basket_app.route('/check-responses', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def check_responses():
    if request.method == 'GET':
        sql_statement = sql_provider.get(
            'check_responses.sql', {'username': session['user']})
        result = select_from_db(
            current_app.config['MYSQL_DB_CONFIG'], sql_statement)

        if not result:
            flash('Нет откликов', 'error')
            return redirect(url_for('access_app.account_settings'))

        return render_template('check_responses.html', responses=result)

    if request.method == 'POST':
        vacancy_id = request.form['vacancy_id']
        username = session['user']

        sql_statement = sql_provider.get('delete_response.sql', {
            'vacancy_id': vacancy_id,
            'username': username
        })

        insert_into_db(current_app.config['MYSQL_DB_CONFIG'], sql_statement)

        flash('Отклик отменен', 'okay')
        return redirect(url_for('basket_app.check_responses'))


@basket_app.route('/view-responses', methods=['GET', 'POST'])
@login_required(session)
@role_required(session)
def view_responses():
    if request.method == 'GET':
        sql_statement = sql_provider.get(
            'view_responses.sql', {})
        result = select_from_db(
            current_app.config['MYSQL_DB_CONFIG'], sql_statement)

        return render_template('view_responses.html', responises=result)

    if request.method == 'POST':
        vacancy_id = request.form['vacancy_id']
        status = request.form['status']
        username = request.form['username']

        sql_statement = sql_provider.get('update_status.sql', {
            'vacancy_id': vacancy_id,
            'username': username,
            'status': status
        })

        insert_into_db(current_app.config['MYSQL_DB_CONFIG'], sql_statement)

        if status == 'Одобрено':
            sql_statement = sql_provider.get('update_vac.sql', {
                'vacancy_id': vacancy_id,
                'date': date.today()
            })

            insert_into_db(
                current_app.config['MYSQL_DB_CONFIG'], sql_statement)

        flash('Статус изменен', 'okay')
        return redirect(url_for('basket_app.view_responses'))
