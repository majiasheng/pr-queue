import constants.http_methods as methods
import os
import handlers

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


@app.route("/help", methods=[methods.GET])
def help():
    return handlers.help()


# TODO: middleware to try catch

@app.route("/list", methods=[methods.GET])
def list_prs():
    # TODO: try catch
    prs = handlers.list_prs(request.args)
    return jsonify(
        data=prs
    )


@app.route("/new", methods=[methods.POST])
def add_new_pr():
    # TODO: try catch
    data = request.get_json()
    result_id = handlers.add_new_pr(data)
    return jsonify(
        data=result_id
    )


@app.route("/close", methods=[methods.DELETE])
def close_pr():
    # TODO: try catch
    data = request.get_json()
    result_id = handlers.close_pr(data)
    return jsonify(
        data=result_id
    )


@app.route("/update", methods=[methods.PUT])
def update_pr():
    # TODO: param
    handlers.update_pr()


if __name__ == '__main__':
    debug = bool(os.environ.get('debug', False))
    app.run(debug=debug)
