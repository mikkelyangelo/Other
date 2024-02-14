from flask import session, request, current_app, redirect, url_for, flash
from functools import wraps


def group_validation(config: dict):
    bp_endpoint = request.endpoint.split('.')[0]
    bp_endpoint_option = request.endpoint.split('.')[1].split('_')[0]
    print(f"{bp_endpoint}.{bp_endpoint_option}")
    if 'group_name' in session:
        group_name = session['group_name']
        if group_name in config and f"{bp_endpoint}.{bp_endpoint_option}" in config[group_name]:
            return True
        return False


def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'login' in session:
            return f(*args, **kwargs)
        else:
            flash('Необходимо авторизоваться', 'error')
            return redirect(url_for('bp_auth.login_page'))
    return wrapper


def group_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        config = current_app.config['ACCESS_CONFIG']
        if group_validation(config):
            return f(*args, **kwargs)
        else:
            flash('У Вас нет доступа к этому варианту использования', 'error')
            return redirect(url_for('home_page'))
    return wrapper
