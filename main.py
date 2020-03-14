__author__ = "ハリネズミ"
from flask import Flask

app = Flask(__name__)
app.config.from_object("config")


@app.route("/hello")
def hello():
    return "hello1"

# app.add_url_rule("/hello", view_func=hello)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port="5000")
