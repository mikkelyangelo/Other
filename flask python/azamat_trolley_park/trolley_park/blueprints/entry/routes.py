
from database import select_dict
from datetime import datetime
from flask import Blueprint, render_template, session, request, current_app, redirect, url_for
from sql_provider import SQLProvider
from blueprints.authorization.access import login_required, auth_required
from database import work_with_db,insert_into_db
import json

entry_app = Blueprint('entry', __name__, template_folder='templates')
db_config = json.load(open('configs/config.json'))
provider = SQLProvider('blueprints/entry/sql/')
basket = {}

@entry_app.route('/', methods=['GET', 'POST'])

def edit_index():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        sql = provider.get('edit_list.sql')

        result = work_with_db(db_config, sql)
        # print(result[0]['account_number'])
        return render_template('edit.html', items=result, heads=["Количество остановок ", "Название пути     ","Дата открытия"])
    else:
        action = request.form.get('action')
        if action == 'Назначить':
            id = request.form.get('id', None)
            session['id'] = id
            # if 'login' in session and session['group_name'] == 'Администратор':
            return redirect('choose')

@entry_app.route('/choose', methods=['GET', 'POST'])
def choose():
    global basket
    if request.method == 'GET':
        sql = provider.get('all_items.sql')
        items = select_dict(db_config, sql)
        # basket = session.get('basket', {})
        print(items)
        return render_template('basket_show.html', item=items, basket=basket, basket_keys=basket.keys())
    else:
        id = request.form.get('id')
        print(id)
        sql = provider.get('add_item.sql', id=id)
        print(sql)
        item = select_dict(db_config, sql)[0]
        add_to_basket(basket, item)
        print(basket)
    return redirect(url_for('entry.choose'))


@entry_app.route('/sec')
def menu():
    global basket
    basket = {}
    return redirect('/second')

@entry_app.route('/clear')
def clear_basket():
    # if 'basket' in session:
    #     session.pop('basket')
    global basket
    basket = {}
    return redirect(url_for('entry.choose'))

def add_to_basket(bask, item):
    # curr_basket = session.get('basket', {})
    # curr_basket[item['ID_Doctor']] = {'Specialization': item['Specialization'],'Surname_D': item['Surname_D'],'Name_D': item['Name_D'], 'Patronymic_D': item['Patronymic_D'], 'amount': 1}
    # session['basket'] = curr_basket
    # session.permanent = True
    # return True
    bask[item['id']] = {'fio': item['fio'], 'birthday': item['birthday'], 'address': item['address'],
                                      'amount': 1}


@entry_app.route('/save_order', methods=['GET', 'POST'])
def save_order():
    global basket
    user_id = session['login']
    id = session['id']
    if basket:
        sql = provider.get('insert_order.sql', user_id=user_id, user_date=datetime.now().strftime("%Y-%m-%d"))
        insert_into_db(db_config, sql)
        sql = provider.get('select_order_id.sql', user_id=user_id)
        # print(insert_into_db(db_config, sql)[0])
        order_id = select_dict(db_config, sql)[0]['max_id']

    for key in basket.keys():
        item = basket[key]
        sql = provider.get('insert_order_list.sql', order_id=order_id, id=key,id_d = id)
        insert_into_db(db_config, sql)
    basket = {}
    return render_template('done.html')
