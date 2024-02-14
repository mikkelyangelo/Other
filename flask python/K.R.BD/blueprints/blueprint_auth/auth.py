from flask import Blueprint, render_template, request, current_app, session, redirect
from work_with_db import select_dict
from sql_provider import SQLProvider
import os

blueprint_auth = Blueprint('bp_auth', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_auth.route('/', methods=['GET', 'POST'])
def auth_reg():
    if request.method == 'GET':
        return render_template('auth.html')
    else:
        login = request.form.get('login')  # объект form - словарь, где ключ - название category, извлекается методом get
        password = request.form.get('password')
        if not login or not password:
            return render_template('auth.html')
        _sql = provider.get('login.sql', login=login, password=password)
        user = select_dict(current_app.config['db_config'], _sql)
        if not user:
            return render_template('need_auth.html')
        else:
            session['user_id'] = user[0]['idUsers']
            session['user_group'] = user[0]['user_group']
            return redirect('/main')


@blueprint_auth.route('/exit', methods=['GET', 'POST'])
def auth_exit():
    session.clear()
    return render_template('start_menu.html')
