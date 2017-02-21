from flask import *
from models.ConnectDatabase import ConnectDatabase
from models.models import *
from peewee import *

db = ConnectDatabase().connect()
app = Flask(__name__)


def init_db():
    if Counter.table_exists() is False:
        db.create_table(Counter, safe=True)


@app.route("/", methods=["GET"])
@app.route("/request-counter", methods=["GET"])
def get_request_counter():
    return render_template("main.html")


@app.route("/request-counter", methods=["POST"])
def post_request_counter():
    return "megy"


@app.route("/statistics", methods=["GET"])
def statistics():
    pass


@app.route("/json-generator", methods=["GET"])
def json_generator():
    pass

if __name__ == "__main__":
    init_db()
    app.run(debug=True)