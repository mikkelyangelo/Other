from functools import wraps
from flask import session, current_app, request, render_template


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        else:
            return "Вам необходимо авторизоваться"

    return wrapper


def group_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' in session:  # в сессии всегда есть 2 ключа,
            # если была авторизация, но у внутр пользователя есть группа, у внешнего None
            user_role = session['user_group']
            if user_role:
                access = current_app.config['access_config']
                user_target = request.blueprint
                user_func = request.endpoint
                if user_role in access and user_target in access[user_role]:
                    return func(*args, **kwargs)
                elif user_role in access and user_func in access[user_role]:
                    # настроить доступ к конкретным обработчикам из blueprint,
                    return func(*args, **kwargs)
                    # надо достать имя обработчика, куда хочет добраться пользователь
                    # request.endpoint -> <имя_blueprint>.request1,
                    # расширить словарь
                else:    # return "Недостаточно прав"  # создать корректные переходы для лр
                    return render_template('need_some.html')
            else:
                return render_template('not_dostup.html')
        else:
            return render_template('need_auth.html')

    return wrapper