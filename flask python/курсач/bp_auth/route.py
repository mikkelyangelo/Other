from flask import Blueprint, render_template, request, current_app, session, flash, redirect, url_for
from db_connect import select_dict
from sql_provider import SQL_Provider


bp_auth = Blueprint('bp_auth', __name__, template_folder='templates', static_folder='static')
provider = SQL_Provider('bp_auth/sql')


@bp_auth.route('/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('auth.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        sql = provider.get_sql('auth.sql', login=login, password=password)
        result = select_dict(current_app.config['DB_CONFIG'], sql)
        if not result:
            flash('Пользователь не найден', 'error')
            return render_template('auth.html')
        session['group_name'], session['login'] = result[0]['user_group'], result[0]['login']
        flash(f"Вы авторизовались как {session['login']}", 'success')
        return redirect(url_for('home_page'))

@bp_auth.route('/logout')
def logout():
    session.pop('group_name', None)
    session.pop('login', None)
    flash('Вы вышли из аккаунта', 'success')
    return redirect(url_for('home_page'))
