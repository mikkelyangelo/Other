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
@login_required
def edit_index():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        return render_template('edit.html', heads=["Номер аккаунта   ", "Баланс     ", "Валюта"])
    else:
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
        return render_template('edit_order.html')
    else:
        quantities = request.form.getlist('quantity[]', None)
        productNames = request.form.getlist('productName[]', None)
        pos = session.get('login') - 3
        sql = provider.get('sql.sql', user_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user=pos)
        insert_into_db(db_config, sql)

        sql2 = provider.get('sql2.sql')
        result = work_with_db(db_config,sql=sql2)
        id = result[0]['max_id']

        for i in range(len(quantities)):
            sql3 = provider.get('sql_get_id.sql',prod_name=productNames[i])
            res1 = work_with_db(db_config,sql3)[0]['Product_id']
            sql4 = provider.get('sql_insert_into_supply.sql',
                                id=id,count_tovar=quantities[i],product_id=res1)
            insert_into_db(db_config, sql4)
            sql5 = provider.get('update_details.sql',count_tovar=quantities[i],tovar_name=productNames[i], user_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            make_update(config=db_config, sql=sql5)

        return redirect('/edit')
