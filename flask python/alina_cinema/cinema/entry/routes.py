from database import select_dict, make_update
from datetime import datetime
from flask import Blueprint, render_template, session, request, current_app, redirect, url_for
from sql_provider import SQLProvider
from database import work_with_db,insert_into_db
import json

entry_app = Blueprint('entry', __name__, template_folder='templates')
db_config = json.load(open('../configs/config.json'))
provider = SQLProvider('../entry/sql/')
basket = {}

@entry_app.route('/', methods=['GET', 'POST'])
def edit_index():
    db_config = current_app.config['db_config']
    if request.method == 'GET':
        sql = provider.get('edit_list.sql')

        result = work_with_db(db_config, sql)
        # print(result[0]['account_number'])
        return render_template('edit.html', items=result, heads=["Дата показа","Страна","Год", "Режиссёр","Студия","Длительность"])
    else:
        action = request.form.get('action')
        if action == 'Купить билет':
            S_ID = request.form.get('S_ID', None)
            session['S_ID'] = S_ID
            return redirect('choose')
            # if 'login' in session and session['group_name'] == 'Администратор':


@entry_app.route('/choose', methods=['GET', 'POST'])
def choose():
    global basket
    if request.method == 'GET':
        S_ID = session.get('S_ID')
        sql = provider.get('all_items.sql', id=S_ID)
        # sql = provider.get('all_items.sql')
        items = select_dict(db_config, sql)
        # basket = session.get('basket', {})
        print(items)
        return render_template('basket_show.html', item=items, basket=basket, basket_keys=basket.keys())
    else:
        T_ID = request.form.get('T_ID')
        print(id)
        sql = provider.get('add_item.sql', id=T_ID)
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
    sql = provider.get('delete.sql')
    make_update(db_config, sql)
    return redirect(url_for('entry.choose'))

def add_to_basket(bask, item):
    # curr_basket = session.get('basket', {})
    # curr_basket[item['ID_Doctor']] = {'Specialization': item['Specialization'],'Surname_D': item['Surname_D'],'Name_D': item['Name_D'], 'Patronymic_D': item['Patronymic_D'], 'amount': 1}
    # session['basket'] = curr_basket
    # session.permanent = True
    # return True
    bask[item['T_ID']] = { 'ROW': item['ROW'],'SIT': item['SIT'], 'PRICE' : item['PRICE'],
                                      'amount': 1}
    sql = provider.get('insert_temp.sql', row=item['ROW'], seat=item['SIT'],
                       price= item['PRICE'], ticket_num=item['T_ID'])
    insert_into_db(db_config, sql)


@entry_app.route('/save_order', methods=['GET', 'POST'])
def save_order():
    global basket
    id = session['S_ID']
    user_id=session['user_id']
    if basket:
        sql = provider.get('insert_order.sql', user_id=user_id, user_date=datetime.now().strftime("%Y-%m-%d"))
        insert_into_db(db_config, sql)
        sql = provider.get('select_order_id.sql', user_id=user_id)
        # print(insert_into_db(db_config, sql)[0])
        order_id = select_dict(db_config, sql)[0]['max_id']

    for key in basket.keys():
        item = basket[key]
        sql1 = provider.get('update_status.sql', id=key)
        make_update(db_config, sql1)
        sql = provider.get('insert_order_list.sql', order_id=order_id, id=key,id_s = id)
        insert_into_db(db_config, sql)
    basket = {}
    return render_template('done.html')
