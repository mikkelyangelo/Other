from flask import Blueprint, render_template, request, current_app
from work_with_db import select_dict
import os
from sql_provider import SQLProvider


blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_query.route('/quest', methods=['GET', 'POST'])
def query_quest1():
    if request.method == 'GET':
        return render_template('quest1.html')


@blueprint_query.route('/quest2', methods=['GET', 'POST'])
def query_quest2():

        _sql = provider.get('client1.sql')
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('dynamic1.html', data=data, title=title)


@blueprint_query.route('/quest3', methods=['GET', 'POST'])
def query_quest3():

        _sql = provider.get('client2.sql')
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('dynamic2.html', data=data, title=title)


@blueprint_query.route('/quest4', methods=['GET', 'POST'])
def query_quest4():

        _sql = provider.get('client3.sql')
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('dynamic3.html', data=data, title=title)


@blueprint_query.route('/quest5', methods=['GET', 'POST'])
def query_quest5():

        _sql = provider.get('client4.sql')
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('dynamic4.html', data=data, title=title)


@blueprint_query.route('/quest6', methods=['GET', 'POST'])
def query_quest6():
    if request.method == 'GET':
        return render_template('input_param1.html')
    else:
        Cost_per_day = request.form.get('Cost_per_day')
        _sql = provider.get('client5.sql', Cost_per_day=Cost_per_day)
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('dynamic5.html', title=title, data=data)
        else:
            a = 'Результата нет'
            return render_template('1.html', a=a)


@blueprint_query.route('/quest7', methods=['GET', 'POST'])
def query_quest7():

    _sql = provider.get('client7.sql')
    data = select_dict(current_app.config['db_config'], _sql)

    if data:
        title = 'Результат'
        return render_template('dynamic6.html', data=data, title=title)

# Сложные запросы

@blueprint_query.route('/quest8', methods=['GET', 'POST'])
def query_quest8():

        _sql = provider.get('hard_otchet1.sql', )
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('hard_otchet1.html', title=title, data=data)
        else:
            a = 'Результата нет'
            return render_template('1.html', a=a)


@blueprint_query.route('/quest9', methods=['GET', 'POST'])
def query_quest9():
    if request.method == 'GET':
        return render_template('inputforhardotchet2.html')
    else:
        start = request.form.get('start')
        finish = request.form.get('finish')
        _sql = provider.get('hard_otchet2.sql', start=start, finish=finish)
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('hard_otchet2.html', title=title, data=data)
        else:
            a = 'Результата нет'
            return render_template('1.html', a=a)


@blueprint_query.route('/quest10', methods=['GET', 'POST'])
def query_quest10():

        _sql = provider.get('hard3.sql')
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('hard3.html', data=data, title=title)


@blueprint_query.route('/quest11', methods=['GET', 'POST'])
def query_quest11():

        _sql = provider.get('hard4.sql')
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('hard4.html', data=data, title=title)


@blueprint_query.route('/quest12', methods=['GET', 'POST'])
def query_quest12():

        _sql = provider.get('hard5.sql')
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('hard5.html', data=data, title=title)


@blueprint_query.route('/quest13', methods=['GET', 'POST'])
def query_quest13():

        _sql = provider.get('hard6.sql')
        data = select_dict(current_app.config['db_config'], _sql)

        if data:
            title = 'Результат'
            return render_template('hard6.html', data=data, title=title)