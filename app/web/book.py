from flask import request

from app.forms.book import SearchForm
from app.libs.util import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel

from . import web


@web.route("/test")
def test1():
    from flask import request
    from app.libs.none_local import n
    print(n.v) # 1
    n.v = 2
    print("--------------")
    print(getattr(request, "v", None)) #None
    setattr(request, 'v', 2)
    print("--------------")
    return ""


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
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        return result
    else:
        return form.errors
