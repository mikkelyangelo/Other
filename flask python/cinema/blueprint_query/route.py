from flask import Blueprint, render_template, request, current_app
from work_with_db import select_dict
from sql_provider import SQLProvider
from access import group_required, login_required
import os

blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_query.route('/choice', methods=['GET', 'POST'])   # самостоятельно blueprint авторизации, форма для логина и пароля. заносить в сессию, поиск пользователя по бд
@group_required
@login_required
def query_choice():
    if request.method == 'GET':
        return render_template('choice.html')


@blueprint_query.route('/sql1', methods=['GET', 'POST'])
@group_required
@login_required
def query_sql1():
    if request.method == 'GET':
        return render_template('sql1.html')
    else:
        data = request.form.get('data')
        if not data:
            return render_template('sql1.html')
        else:
            _sql = provider.get('sql1.sql', data=data)
        products = select_dict(current_app.config['db_config'], _sql)
        if products:
            prod_title = 'ПОЛУЧЕННЫЙ РЕЗУЛЬТАТ'
            return render_template('data.html', products=products, prod_title=prod_title)
        else:
            return render_template('not_found.html')


@blueprint_query.route('/sql2', methods=['GET', 'POST'])
@group_required
@login_required
def query_sql2():
    if request.method == 'GET':
        return render_template('sql2.html')
    else:
        month = request.form.get('month')
        year = request.form.get('year')
        if not month and year:
            return render_template('sql2.html')
        elif not month and not year:
            return render_template('sql2.html')
        elif month and not year:
            return render_template('sql2.html')
        else:
            _sql = provider.get('sql2.sql', month=month, year=year)
        products = select_dict(current_app.config['db_config'], _sql)
        if products:
            prod_title = 'ПОЛУЧЕННЫЙ РЕЗУЛЬТАТ'
            return render_template('difference.html', products=products, prod_title=prod_title)
        else:
            return render_template('not_found.html')


@blueprint_query.route('/sql3', methods=['GET', 'POST'])
@group_required
@login_required
def query_sql3():
        _sql = provider.get('sql3.sql')
        products = select_dict(current_app.config['db_config'], _sql)
        if products:
            prod_title = 'ПОЛУЧЕННЫЙ РЕЗУЛЬТАТ'
            print(products)
            return render_template('kolvo.html', products=products, prod_title=prod_title)
        else:
            return render_template('not_found.html')

@blueprint_query.route('/sql4', methods=['GET', 'POST'])
@group_required
@login_required
def query_sql4():
        _sql = provider.get('sql4.sql')
        products = select_dict(current_app.config['db_config'], _sql)
        if products:
            prod_title = 'ПОЛУЧЕННЫЙ РЕЗУЛЬТАТ'
            return render_template('ticket.html', products=products, prod_title=prod_title)
        else:
            return render_template('not_found.html')

@blueprint_query.route('/sql5', methods=['GET', 'POST'])
@group_required
@login_required
def query_sql5():
    if request.method == 'GET':
        return render_template('sql5.html')
    else:
        year = request.form.get('year')
        if not year:
            return render_template('sql5.html')
        else:
            _sql = provider.get('sql5.sql', year=year)
        products = select_dict(current_app.config['db_config'], _sql)
        if products:
            prod_title = 'Полученный результат'
            return render_template('max.html', products=products, prod_title=prod_title)
        else:
            return render_template('not_found.html')

@blueprint_query.route('/sql6', methods=['GET', 'POST'])
@group_required
@login_required
def query_sql6():
    if request.method == 'GET':
        return render_template('sql5.html')
    else:
        _sql = provider.get('sql6.sql')
        year = request.form.get('year')
        if not year:
            return render_template('sql5.html')
        else:
            _sql = provider.get('sql6_2.sql', year=year)
        products = select_dict(current_app.config['db_config'], _sql)
        if products:
            prod_title = 'Полученный результат'
            return render_template('categ.html', products=products, prod_title=prod_title)
        else:
            return render_template('not_found.html')