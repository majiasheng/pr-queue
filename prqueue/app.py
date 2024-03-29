import constants.http_methods as methods
import os
import handlers

from functools import wraps
from dotenv import load_dotenv
from persistence.db_manager import get_engine, get_sqlite_engine
from flask import Flask, request, jsonify

load_dotenv()
app = Flask(__name__)
# db_engine = get_engine()
db_engine = get_sqlite_engine()

if os.environ.get('env', 'development') == 'development':
    import init
    init.init_app(db_engine)


def returns_json(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return jsonify(func(*args, **kwargs))
        except Exception as e:
            return jsonify(
                {'error': str(e)}
            )

    return inner

@app.route("/help", methods=[methods.GET])
def help():
    return handlers.help()


@app.route("/peek", methods=[methods.GET])
@returns_json
def peek():
    return handlers.peek()


@app.route("/list", methods=[methods.GET])
@returns_json
def list_prs():
    return handlers.list_prs(request.args)


@app.route("/new", methods=[methods.POST])
@returns_json
def add_new_pr():
    data = request.get_json()
    result_id = handlers.add_new_pr(data)
    return {'id': result_id}


@app.route("/close", methods=[methods.DELETE])
@returns_json
def close_pr():
    data = request.get_json()
    res = {
        'success': False
    }

    success = handlers.close_pr(data)
    if success:
        res['success'] = True
    return res


@app.route("/update", methods=[methods.PUT])
def update_pr():
    # TODO: param
    handlers.update_pr()


if __name__ == '__main__':
    debug = bool(os.environ.get('debug', False))
    app.run(debug=debug)
