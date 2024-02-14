import os

from flask import Blueprint, request, render_template, session, current_app
from werkzeug.utils import redirect
from datetime import datetime
from database import work_with_db, make_update, insert_into_db
from sql_provider import SQLProvider
from blueprints.authorization.access import login_required, auth_required


edit_app = Blueprint('edit', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@edit_app.route('/', methods=['POST', 'GET'])
@auth_required
def edit_index():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        if session['group_name'] == 'client1':
            id = 1
        if session['group_name'] == 'client2':
            id = 2
        if session['group_name'] == 'client3':
            id = 3
        if session['group_name'] == 'client4':
            id = 4
        if session['group_name'] == 'client5':
            id = 5
        if session['group_name'] == 'client6':
            id = 6
        sql = provider.get('edit_list.sql', cliend_id=id)

        result = work_with_db(db_config, sql)
        # print(result[0]['account_number'])
        return render_template('edit.html', items=result, heads=["Номер аккаунта   ", "Баланс     ", "Валюта"])
    else:
        action = request.form.get('action')
        if action == 'Перевести':
            id = request.form.get('id', None)
            balance=request.form.get('balance', None)
            account_number = request.form.get('account_number', None)
            session['id'] = id
            session['balance'] = balance
            session['account_number'] = account_number
            # if 'login' in session and session['group_name'] == 'Администратор':
            return redirect('edit_order')
        if action == 'Удалить':
            id = request.form.get('id', None)
            sql = provider.get('delete_edit.sql', id=id)
            make_update(config=db_config, sql=sql)
            # return redirect('/edit')
            return render_template('edit.html')


@edit_app.route('/add', methods=['POST', 'GET'])
def add_edit():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        return render_template('insert_item.html')
    else:
        theme = request.form.get('theme', None)
        sql = provider.get('insert_edit.sql', theme=theme)
        make_update(config=db_config, sql=sql)

        return redirect('/edit')


@edit_app.route('/edit_order', methods=['POST', 'GET'])
def edit_order():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        card_id = session['id']
        sql = provider.get('get_info_orders.sql', card_id=card_id)
        item = work_with_db(config=db_config, sql=sql)
        return render_template('edit_order.html', item=item[0])
    else:
        rek = request.form.get('rek', None)
        sum = request.form.get('sum', None)
        currency_0 = request.form.get('currency', None)
        sql_0 = provider.get('sql_0.sql', acc=rek)
        result = work_with_db(db_config, sql_0)
        print(result[0]['currency'])
        print(result[0]['idaccount'])
        print(result[0]['balance'])
        idaccount=result[0]['idaccount']
        balance2=result[0]['balance']
        exchange_rate = 50
        if currency_0 == result[0]['currency']:
                exchange_rate = 1
        elif currency_0 == 'RUB' and result[0]['currency'] == 'USD':
            exchange_rate = 1/50
        print(exchange_rate)
        account_number = session['account_number']
        # account_n = request.form.get('account_number', None)
        card_id = session['id']
        balance = session['balance']
        new_balance = int(balance) - int(sum)
        new_balance2 = int(balance2) + int(sum) * exchange_rate
        sql = provider.get('edit_for_students.sql',
                           account_n=account_number,sum=sum,
                           card_id=card_id)

        sql_insert1 = provider.get('insert_1.sql',id=card_id,balance=balance,new_balance=new_balance,balance_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        insert_into_db(db_config, sql_insert1)
        make_update(config=db_config, sql=sql)
        sql2 = provider.get('edit_order.sql', rek=rek,
                           sum=sum,exchange_rate=exchange_rate)
        sql_insert2 = provider.get('insert_2.sql',id=idaccount,balance=balance2,new_balance=new_balance2,balance_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        insert_into_db(db_config, sql_insert2)
        make_update(config=db_config, sql=sql2)



        return redirect('/edit')
