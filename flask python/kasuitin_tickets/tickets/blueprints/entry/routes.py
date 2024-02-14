from database import select_dict, make_update
from datetime import datetime
from flask import Blueprint, render_template, session, request, current_app, redirect, url_for
from sql_provider import SQLProvider
from blueprints.authorization.access import login_required, auth_required
from database import work_with_db, insert_into_db
import json

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
        return render_template('edit.html', items=result, heads=["дата рейса", "Отправление     ", "Прибытие"])
    else:
        action = request.form.get('action')
        if action == 'Купить билет':
            # theme = request.form.get('theme',None)
            # session['theme'] = theme
            id_flight = request.form.get('id', None)
            session['id'] = id_flight
            # if 'login' in session and session['group_name'] == 'Администратор':
            return redirect('choose')


@entry_app.route('/choose', methods=['GET', 'POST'])
def choose():
    global basket
    if request.method == 'GET':
        id_flight = session['id']
        sql = provider.get('all_items.sql', id=id_flight)
        items = select_dict(db_config, sql)
        # basket = session.get('basket', {})
        print(items)
        # if items is not None:
        return render_template('basket_show.html', item=items, basket=basket, basket_keys=basket.keys())
        # else:
        #     return redirect('/entry')
    else:
        id = request.form.get('id')
        # id_dep = request.form.get('id_dep')
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
    sql = provider.get('delete.sql')
    make_update(db_config, sql)
    return redirect(url_for('entry.choose'))


def add_to_basket(bask, item):
    # curr_basket = session.get('basket', {})
    # curr_basket[item['ID_Doctor']] = {'Specialization': item['Specialization'],'Surname_D': item['Surname_D'],'Name_D': item['Name_D'], 'Patronymic_D': item['Patronymic_D'], 'amount': 1}
    # session['basket'] = curr_basket
    # session.permanent = True
    # return True
    bask[item['id_ticket']] = {'class': item['class'], 'cost': item['cost'],
                        'bonus_add': item['bonus_add'],
                        'amount': 1}
    sql = provider.get('insert_temp.sql', id_ticket=item['id_ticket'], cost=item['cost'], dclass=item['class'],bonus=item['bonus_add'])
    insert_into_db(db_config, sql)


@entry_app.route('/save_order', methods=['GET', 'POST'])
def save_order():
    global basket
    if request.method == 'GET':
        if basket:
            user_id=session['login']
            sql_bonus = provider.get('get_data.sql',user_id=user_id-3)
            bonuses = select_dict(db_config, sql_bonus)[0]['bonuses']

            sql0 = provider.get('sum.sql')
            sum = select_dict(db_config, sql0)[0]['sum']

            sql_temp = provider.get('sum_bonus.sql')
            bonus = select_dict(db_config, sql_temp)[0]['bonus']

            session['bonus'] = bonus
            session['bonuses'] = bonuses
            print(sum)
            print(bonuses)
            if bonuses >= sum:
                required = sum
            elif sum > bonuses:
                required = bonuses
            return render_template('choose_payment.html', sum=sum, bonuses=bonuses, required=required)
        else:
            return render_template('not_done.html')
    else:
        action = request.form.get('action')
        if action == 'Заплатить деньгами':
            bonus = session['bonus']
            bonuses = session['bonuses']
            user_id = session['login']

            sql_pass = provider.get('update_pass.sql', bonus=bonus, user_id=user_id - 3)
            make_update(db_config, sql_pass)

            for key in basket.keys():
                item = basket[key]
                sql1 = provider.get('update_status.sql', id=key,user_id=user_id-3,user_date=datetime.now().strftime("%Y-%m-%d"))
                make_update(db_config, sql1)

            sql = provider.get('insert_balance.sql', user_id=user_id-3, user_date=datetime.now().strftime("%Y-%m-%d"),
                               bonus=bonuses, bonuses=int(bonuses) + int(bonus))
            insert_into_db(db_config, sql)

            basket = {}
            sql = provider.get('delete.sql')
            make_update(db_config, sql)

            return render_template('done.html')
        elif action == 'Купить билет':
            bonuses = session['bonuses']
            user_id = session['login']
            bonuss=request.form.get('bonuss',None)

            sql_pass = provider.get('update_pass2.sql', bonus=bonuss, user_id=user_id - 3)
            make_update(db_config, sql_pass)

            for key in basket.keys():
                item = basket[key]
                sql1 = provider.get('update_status.sql', id=key, user_id=user_id - 3,user_date=datetime.now().strftime("%Y-%m-%d"))
                make_update(db_config, sql1)

            sql = provider.get('insert_balance.sql', user_id=user_id - 3, user_date=datetime.now().strftime("%Y-%m-%d"),
                               bonus=bonuses, bonuses=int(bonuses) - int(bonuss))
            insert_into_db(db_config, sql)

            basket = {}
            sql = provider.get('delete.sql')
            make_update(db_config, sql)

            return render_template('done.html')
