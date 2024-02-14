import os

from flask import Blueprint, request, render_template, session, current_app, url_for
from werkzeug.utils import redirect
from datetime import datetime
from database import work_with_db, make_update, insert_into_db, select_dict
from sql_provider import SQLProvider
# from blueprints.authorization.access import login_required, auth_required


edit_app = Blueprint('edit', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
basket = {}


@edit_app.route('/', methods=['POST', 'GET'])
def edit_index():
    db_config = current_app.config['db_config']
    if request.method == 'GET':
        ids = 1
        if session['user_group'] == 'client1':
            ids = 1
        if session['user_group'] == 'client2':
            ids = 2
        if session['user_group'] == 'client3':
            ids = 3
        if session['user_group'] == 'client4':
            ids = 4
        if session['user_group'] == 'client5':
            ids = 5
        print(session['user_group'])
        session['id'] = ids
        sql = provider.get('edit_list.sql', ids=ids)

        result = work_with_db(db_config, sql)
        # print(result[0]['account_number'])
        return render_template('edit.html', items=result, heads=["Дата подключения   ", "Имя провайдера    ", "Плата в день","Дата отключения услуги"])
    else:
        action = request.form.get('action')
        # if action == 'Перевести':
        #     id = request.form.get('', None)
        #     balance=request.form.get('balance', None)
        #     account_number = request.form.get('account_number', None)
        #     session['id'] = id
        #     session['balance'] = balance
        #     session['account_number'] = account_number
        #     # if 'login' in session and session['group_name'] == 'Администратор':
        #     return redirect('edit_order')
        if action == 'Отказаться от провайдера':
            id = request.form.get('idService_connection_and_disconnection_history', None)
            sql = provider.get('delete_edit.sql', id=id, user_date=datetime.now().strftime("%Y-%m-%d"))
            make_update(config=db_config, sql=sql)
            # return redirect('/edit')
            return redirect(url_for('edit.edit_index'))

@edit_app.route('/choose', methods=['GET', 'POST'])
def choose():
    global basket
    db_config = current_app.config['db_config']
    if request.method == 'GET':
        ids = session['id']
        sql = provider.get('all_items.sql', id=ids)
        items = select_dict(db_config, sql)
        # basket = session.get('basket', {})
        print(items)
        # if items is not None:
        return render_template('basket_show.html', item=items, basket=basket, basket_keys=basket.keys())
        # else:
        #     return redirect('/entry')
    else:
        id = request.form.get('idService')
        # id_dep = request.form.get('id_dep')
        print(id)
        sql = provider.get('add_item.sql', id=id)
        print(sql)
        item = select_dict(db_config, sql)[0]
        add_to_basket(basket, item)
        print(basket)
    return redirect(url_for('edit.choose'))


@edit_app.route('/sec')
def menu():
    global basket
    basket = {}
    return redirect('/second')


@edit_app.route('/clear')
def clear_basket():
    db_config = current_app.config['db_config']
    # if 'basket' in session:
    #     session.pop('basket')
    global basket
    basket = {}
    sql = provider.get('delete.sql')
    make_update(db_config, sql)
    return redirect(url_for('edit.choose'))


def add_to_basket(bask, item):
    db_config = current_app.config['db_config']
    # curr_basket = session.get('basket', {})
    # curr_basket[item['ID_Doctor']] = {'Specialization': item['Specialization'],'Surname_D': item['Surname_D'],'Name_D': item['Name_D'], 'Patronymic_D': item['Patronymic_D'], 'amount': 1}
    # session['basket'] = curr_basket
    # session.permanent = True
    # return True
    bask[item['idService']] = {'Name': item['Name'], 'Cost_per_day': item['Cost_per_day'],
                        'amount': 1}
    sql = provider.get('insert_temp.sql', Name=item['Name'], Cost_per_day=item['Cost_per_day'],
                       idService=item['idService'])
    insert_into_db(db_config, sql)


@edit_app.route('/save_order', methods=['GET', 'POST'])
def save_order():
    db_config = current_app.config['db_config']
    global basket
    id = session['id']
    # if basket:
    #     sql = provider.get('insert_order.sql', user_id=user_id, user_date=datetime.now().strftime("%Y-%m-%d"))
    #     insert_into_db(db_config, sql)
    #     sql = provider.get('select_order_id.sql', user_id=user_id)
    #     # print(insert_into_db(db_config, sql)[0])
    #     order_id = select_dict(db_config, sql)[0]['max_id']

    for key in basket.keys():
        item = basket[key]
        # sql1 = provider.get('update_status.sql', id=key)
        # # sql2 = provider.get('get_cash.sql', id=item['id_dep'])
        # make_update(db_config, sql1)
        sql = provider.get('insert_order_list.sql', id_cl=id, user_date=datetime.now().strftime("%Y-%m-%d"), id_serv=key)
        insert_into_db(db_config, sql)
    basket = {}
    sql = provider.get('delete.sql')
    make_update(db_config, sql)
    return render_template('done.html')



