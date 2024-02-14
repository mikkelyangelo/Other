from database import select_dict, make_update
from datetime import datetime
from flask import Blueprint, render_template, session, request, current_app, redirect, url_for
from sql_provider import SQLProvider
from blueprints.authorization.access import login_required, auth_required
from database import work_with_db,insert_into_db
import json
import numpy as np

entry_app = Blueprint('entry', __name__, template_folder='templates')
db_config = json.load(open('configs/config.json'))
provider = SQLProvider('blueprints/entry/sql/')
basket = {}

@entry_app.route('/', methods=['GET', 'POST'])
@auth_required
@login_required
def edit_index():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        sql = provider.get('edit_list.sql')

        result = work_with_db(db_config, sql)
        # print(result[0]['account_number'])
        return render_template('edit.html', items=result, heads=["Дата показа", "Режиссёр","Студия"])
    else:
        action = request.form.get('action')
        if action == 'Купить':
            ID_seansa = request.form.get('ID_seansa', None)
            session['ID_seansa'] = ID_seansa
            return redirect('choose')
            # if 'login' in session and session['group_name'] == 'Администратор':


def get_seat_status(row, seat):

    query = "SELECT status FROM tickets WHERE row = %s AND seat = %s"
    result = work_with_db(db_config, query)

    status = result[0]['status']  # Предполагается, что статус находится в первом столбце результата запроса

    return status

@entry_app.route('/choose', methods=['GET', 'POST'])
def choose():
    global basket
    if request.method == 'GET':
        ID_seansa = session.get('ID_seansa')
        sql = provider.get('all_items.sql',id=ID_seansa)
        sql2 = provider.get('all_items2.sql',id=ID_seansa)
        sql3 = provider.get('all_items3.sql',id=ID_seansa)

        items = select_dict(db_config, sql)
        items2 = select_dict(db_config,sql2)
        res = select_dict(db_config,sql3)
        # basket = session.get('basket', {})
        quit = 1
        if res is not None:
            max_row = res[0]['max_row']
            max_seat = res[0]['max_seat']
            status = np.zeros((max_row, max_seat))
            for i in range(max_row):
                for j in range(max_seat):
                    stop = 0
                    for t in items2:
                        print(t['row'])
                        if t['row'] == i + 1 and t['seat'] == j + 1:
                            stat = t['status']
                            status[i][j] = stat
                            stop = 1
                        if stop == 1:
                            break
            print(status[2][0])
            print(items)
            print(status)
            return render_template('basket_show.html', item=items, basket=basket,
                                   basket_keys=basket.keys(), max_row=max_row, max_seat=max_seat, quit=quit, status=status)
        else:
            return render_template('basket_show.html', item=items, basket=basket,
                                   basket_keys=basket.keys(), quit=0)
    else:
        ID_ticket = request.form.get('ID_ticket')
        print(id)
        sql = provider.get('add_item.sql', id=ID_ticket)
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
    bask[item['ID_ticket']] = { 'row': item['row'],'seat': item['seat'], 'price' : item['price'],
                                      'amount': 1}
    sql = provider.get('insert_temp.sql', row=item['row'], seat=item['seat'],
                       price=item['price'], ticket_num=item['ID_ticket'])
    insert_into_db(db_config, sql)


@entry_app.route('/save_order', methods=['GET', 'POST'])
def save_order():
    global basket
    user_id = session['login']
    id = session['ID_seansa']
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
        sql = provider.get('insert_order_list.sql', order_id=order_id, id=key,id_d = id)
        insert_into_db(db_config, sql)
    basket = {}
    return render_template('done.html')
