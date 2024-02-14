import os

from flask import Blueprint, request, render_template, session, current_app, url_for
from werkzeug.utils import redirect

from database import work_with_db, make_update
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
        # id = request.form.get('id', None)
        sql = provider.get('edit_list.sql')

        result = work_with_db(db_config, sql)
        # print(result[0]['account_number'])
        print(session['group_name'])
        if session['group_name'] == 'Администратор' or session['group_name'] == 'Работник':
            return render_template('edit.html', items=result, log=1,
                                   heads=["Вип статус  ", "количество посадочных мест    ",
                                          "Курящий зал", "Имя заказчика", "время резерва","кто создал заказ"])
        else:
            return render_template('edit.html', items=result, log=0)

    else:
        action = request.form.get('action')
        if action == 'Назначить столик':
            id = request.form.get('id', None)
            col = request.form.get('count_seats', None)
            session['id'] = id
            session['count_seats'] = col
            # if 'login' in session and session['group_name'] == 'Администратор':
            return redirect('edit_order')
        if action == 'Отменить бронирование':
            id = request.form.get('id', None)
            sql_update=provider.get('update.sql' ,id=id)
            # sql_update2=provider.get('update2.sql',id=id)
            make_update(config=db_config, sql=sql_update)
            # make_update(config=db_config, sql=sql_update2)
            sql = provider.get('delete_edit.sql', id=id)
            make_update(config=db_config, sql=sql)
            # return redirect('/edit')
            return redirect(url_for('edit.edit_index'))


@edit_app.route('/add', methods=['POST', 'GET'])
def add_edit():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        return render_template('insert_item.html')
    else:
        checkbox = request.form.get('checkbox', 0)
        checkbox2 = request.form.get('checkbox2', 0)
        count_guest = request.form.get('count_guest', None)
        time_res = request.form.get('time_res', None)
        name1 = request.form.get('name', None)
        if session['group_name'] == 'Клиент':
            who='клиент'
        else:
            who='работник'
        sql = provider.get('insert_edit.sql', names=name1,
                           checkbox=checkbox,checkbox2=checkbox2,
                           count_guest=count_guest, time_res=time_res,who=who)
        make_update(config=db_config, sql=sql)

        return redirect('/edit')


@edit_app.route('/edit_order', methods=['POST', 'GET'])
def edit_order():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        col = session['count_seats']
        sql = provider.get('get_info_orders.sql', col=col)
        item = work_with_db(config=db_config, sql=sql)
        return render_template('edit_order.html', items=item, log=1)
    else:
        action = request.form.get('action', None)
        if action == 'Выбрать столик для брони':
            id = request.form.get('id', None)
            idres = session['id']
            sql = provider.get('update3.sql',id=id,idres=idres)
            make_update(config=db_config, sql=sql)
            sql2 = provider.get('update2.sql',idres=idres)
            make_update(config=db_config, sql=sql2)
            return redirect('/edit')
        return redirect('/edit')
