import os

from flask import Blueprint, request, render_template, session, current_app
from werkzeug.utils import redirect

from database import work_with_db, make_update
from sql_provider import SQLProvider


edit_app = Blueprint('edit', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@edit_app.route('/', methods=['POST', 'GET'])
def edit_index():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        sql = provider.get('edit_list.sql')
        result = work_with_db(config=db_config, sql=sql)

        return render_template('edit.html', items=result, heads=["Имя", "Номер авто", "Дата", "Стоимость ТО"])
    else:
        action = request.form.get('action')
        if action == 'Изменить':
            IDzak = request.form.get('IDzak', None)
            session['IDzak'] = IDzak
            return redirect('edit_order')
        sort = request.form.get('sort')

        if sort == 'Отсортировать':
            sql = provider.get('edit_list_sort.sql')
            result = work_with_db(config=db_config, sql=sql)
            render_template('edit.html', items=result, heads=["Имя", "Номер авто", "Дата", "Стоимость ТО"])
            return render_template('edit.html', items=result, heads=["Имя", "Номер авто", "Дата", "Стоимость ТО"])

        IDzak = request.form.get('IDzak', None)
        sql = provider.get('delete_edit.sql', IDzak=IDzak)
        make_update(config=db_config, sql=sql)
        return redirect('/edit')



@edit_app.route('/edit_order', methods=['POST', 'GET'])
def edit_order():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        IDzak = session['IDzak']
        sql = provider.get('get_info_orders.sql', IDzak=IDzak)
        item = work_with_db(config=db_config, sql=sql)
        return render_template('edit_order.html', item=item[0])
    else:
        DateTO = request.form.get('DateTO', None)
        NumAU = request.form.get('NumAU', None)
        Cli = request.form.get('Cli', None)
        CostTO = request.form.get('CostTO', None)
        IDzak = session['IDzak']
        sql = provider.get('edit_order.sql', DateTO=DateTO, NumAU=NumAU, Cli=Cli, CostTO=CostTO, IDzak=IDzak)
        make_update(config=db_config, sql=sql)

        return redirect('/edit')
