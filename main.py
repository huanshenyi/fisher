__author__ = "ハリネズミ"
from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello1"

# app.add_url_rule("/hello", view_func=hello)


app.run(host="0.0.0.0", debug=True, port="5000")
