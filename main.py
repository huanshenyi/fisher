__author__ = "ハリネズミ"

import json

from flask import Flask, jsonify
from util import is_isbn_or_key

from yushu_book import YuShuBook

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
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port="5000")
