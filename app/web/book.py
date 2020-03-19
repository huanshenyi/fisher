from flask import request

from app.forms.book import SearchForm
from util import is_isbn_or_key
from yushu_book import YuShuBook

from . import web


@web.route("/book/search")
def search():
    """
        q: isbn && 普通のキーワード
        page(start, count)
        別の例: ?q=作家名&page=1
    :return:
    """
    # クライアントからのパラメータを制限かける
    # 長さの制限かける
    # q = request.args["q"]
    # 整数である、最大値制限をかける
    # page = request.args["page"]
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return result
    else:
        return form.errors
