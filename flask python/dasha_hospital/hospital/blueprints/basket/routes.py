import os, json
from flask import Blueprint, render_template, session, request, current_app, redirect
from database import work_with_db, make_update
from sql_provider import SQLProvider
from .utils import add_to_basket, clear_basket

basket_app = Blueprint('basket', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@basket_app.route('/', methods=['GET', 'POST'])
def order_list_handler():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        current_basket = session.get('basket', [])
        sql = provider.get('order_list.sql')
        items = work_with_db(db_config, sql)
        return render_template('basket_order_list.html', items=items, basket=current_basket)
    else:
        item_id = request.form['id']
        sql = provider.get('order_item.sql', tickets_id=item_id)
        items = work_with_db(db_config, sql)
        if not items:
            return 'Item not found'
        add_to_basket(items)
        return redirect('/basket')


@basket_app.route('/buy')
def buy_basket_handler():
    basket = session.get('basket', [])
    client_id = session.get('client_id', [])
    db_config = current_app.config['DB_CONFIG']
    for item in basket:
        item_name = item.get('tickets_id')
        sql = provider.get('insert_order.sql', orders_client=client_id)
        make_update(db_config, sql)
        sql = provider.get('select_max_order.sql')
        order_id = work_with_db(db_config, sql)
        sql = provider.get('insert_tickets.sql', tickets_id=item_name, orders_id=order_id[-1]['MAX(orders_id)'])
        make_update(db_config, sql)
    clear_basket()
    return redirect('/')


@basket_app.route('/clear')
def clear_basket_handler():
    clear_basket()
    return redirect('/basket')
