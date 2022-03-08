import constants.http_methods as methods
import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()
app = Flask(__name__)


@app.route("/help", methods = [methods.GET])
def help():
    return "<p>pr-queue LINK-TO-PULL-REQUEST</p>"


@app.route("/list", methods = [methods.GET])
def list_prs():
    pass


@app.route("/new", methods = [methods.POST])
def add_new_pr():
    pass

@app.route("/close", methods = [methods.DELETE])
def close_pr():
    pass

@app.route("/update", methods = [methods.PUT])
def update_pr():
    pass


if __name__ == '__main__':
    debug = bool(os.environ.get('debug', False))
    app.run(debug = debug)
