__author__ = "ハリネズミ"
from flask import Flask, make_response
from util import is_isbn_or_key

app = Flask(__name__)
app.config.from_object("config")


@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
        q: isbn && 普通のキーワード
        page(start, count)
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port="5000")
