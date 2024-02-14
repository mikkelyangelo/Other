from flask import (
	Blueprint, render_template,
	request, current_app,
	session, redirect, url_for
)
from database import select_dict
from sql_provider import SQLProvider
from cache.wrapper import fetch_from_cache


bp_basket = Blueprint('basket', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider('blueprints/basket/sql/')


@bp_basket.route('/', methods=['GET', 'POST'])
def basket_index():
	db_config = current_app.config['DB_CONFIG']
	cache_config = current_app.config['CACHE_CONFIG']
	cached_func = fetch_from_cache('all_items_cached', cache_config)(select_dict)
	sql = provider.get('all_items.sql')
	items = cached_func(db_config, sql)
	if request.method == 'GET':
		basket_items = session.get('basket', {})
		return render_template('index.html', items=items, basket_items=basket_items)
	else:
		prod_id = request.form['prod_id']
		item_description = [item for item in items if str(item['prod_id']) == str(prod_id)]
		item_description = item_description[0]
		curr_basket = session.get('basket', {})

		if prod_id in curr_basket:
			curr_basket[prod_id]['amount'] = curr_basket[prod_id]['amount'] + 1
		else:
			curr_basket[prod_id] = {
				'name': item_description['name'],
				'price': item_description['price'],
				'amount': 1
			}
		session['basket'] = curr_basket
		session.permanent = True

		return redirect(url_for('basket.basket_index'))


@bp_basket.route('/clear-basket')
def clear_basket():
	if 'basket' in session:
		session.pop('basket')
	return redirect(url_for('basket.basket_index'))

@bp_basket.route('/order')
def order():
	sum = 0
	for item in session.get('basket').values():
		sum += item['amount'] * item['price']

	sql_order = provider.get('new_order.sql', user_id=session['user_id'], sum=sum)
	select_dict(current_app.config['DB_CONFIG'], sql_order)
	for key, value in session['basket'].items():
		sql_basket = provider.get('new_order_line.sql', prod_id=key, amount=value['amount'])
		select_dict(current_app.config['DB_CONFIG'], sql_basket)
	session.pop('basket')
	return render_template('order.html', sum=sum)