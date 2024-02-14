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
        # print(result[0]['account_number'])
        return render_template('edit.html')


@entry_app.route('/add', methods=['POST', 'GET'])
def add_edit():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        return render_template('insert_item.html')
    else:
        doc_name = request.form.get('doc_name', None)
        shifr = request.form.get('shifr', None)
        date_of_arrive = request.form.get('date_of_arrive', None)
        session['doc_name'] = doc_name
        session['shifr'] = shifr
        session['date_of_arrive'] = date_of_arrive

        return redirect('/entry/edit_order')


@entry_app.route('/edit_order', methods=['POST', 'GET'])
def edit_order():
    db_config = current_app.config['DB_CONFIG']
    if request.method == 'GET':
        return render_template('edit_order.html')
    else:
        doc_name = session.get('doc_name')
        shifr = session.get('shifr')
        date_of_arrive = session.get('date_of_arrive')
        crew_id = request.form.get('crew_id', None)
        sql = provider.get('sql.sql',date_of_arrive=date_of_arrive,doc_name=doc_name,shifr=shifr,crew_id=crew_id)
        insert_into_db(db_config, sql)
    return redirect('/entry')