import constants.http_methods as methods
import os
import handlers
import init

from dotenv import load_dotenv
from db.db_manager import get_engine, get_sqlite_engine
from flask import Flask

load_dotenv()
app = Flask(__name__)
# db_engine = get_engine()
db_engine = get_sqlite_engine()

init.init_app()

@app.route("/help", methods = [methods.GET])
def help():
    return handlers.handle_help()


@app.route("/list", methods = [methods.GET])
def list_prs():
    handlers.handle_list_prs()


@app.route("/new", methods = [methods.POST])
def add_new_pr():
    # TODO: param
    handlers.handle_add_new_pr()

@app.route("/close", methods = [methods.DELETE])
def close_pr():
    handlers.handle_close_pr()

@app.route("/update", methods = [methods.PUT])
def update_pr():
    # TODO: param
    handlers.handle_update_pr()


if __name__ == '__main__':
    debug = bool(os.environ.get('debug', False))
    app.run(debug = debug)
