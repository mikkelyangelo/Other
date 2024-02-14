from flask import Blueprint, render_template, request, current_app
from db_connect import select_dict
from sql_provider import SQL_Provider
import access


bp_queries = Blueprint('bp_queries', __name__, template_folder='templates', static_folder='static')
provider = SQL_Provider('bp_queries/sql')


def word_end(word):
    if str(word)[-1] == 'т':
        return 'ы'
    return 'и'

@bp_queries.route('/')
@access.auth_required
@access.group_required
def search_choice():
    return render_template('search_choice.html')

@bp_queries.route('/tmtbl', methods=['GET', 'POST'])
def tmtbl():
    if request.method == 'GET':
        return render_template('input_tmtbl.html')
    else:
        snp = request.form.get('snp')
        date = request.form.get('date')
        sql = provider.get_sql('tmtbl.sql', snp=snp, date=date)
        tmtbls = select_dict(current_app.config['db_config'], sql)
        return render_template('results_tmtbl.html', res_title=f"{snp.title()}: расписание на {date}",
                               result=tmtbls)

@bp_queries.route('/patient_hist', methods=['GET', 'POST'])
def patient_hist():
    if request.method == 'GET':
        return render_template('input_patient_hist.html')
    else:
        snp = request.form.get('snp')
        sql = provider.get_sql('patient_hist.sql', snp=snp)
        hist = select_dict(current_app.config['db_config'], sql)
        return render_template('results_patient_hist.html', res_title=f"История обращений пациента {snp.title()}",
                               result=hist)


# @bp_queries.route('/docs', methods=['GET', 'POST'])
# def docs():
#     if request.method == 'GET':
#         return render_template('input_docs.html')
#     else:
#         specialization = request.form.get('specialization')
#         sql = provider.get_sql('docs.sql', specialization=specialization)
#         doctors = select_dict(current_app.config['db_config'], sql)
#         return render_template('results_docs.html', res_title=f"Все врачи-{specialization}{word_end(specialization)}",
#                                result=doctors, specialization=specialization)
#
# @bp_queries.route('/doc_tmtbl', methods=['GET', 'POST'])
# def doc_tmtbl():
#     if request.method == 'GET':
#         return render_template('input_doc_tmtbl.html')
#     else:
#         snp = request.form.get('snp')
#         date = request.form.get('date')
#         sql = provider.get_sql('doc_tmtbl.sql', snp=snp, date=date)
#         doc_tmtbls = select_dict(current_app.config['db_config'], sql)
#         return render_template('results_doc_tmtbl.html', res_title=f"{snp.title()}: свободные часы {date}",
#                                result=doc_tmtbls)