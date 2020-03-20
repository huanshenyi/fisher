__author__ = "ハリネズミ"
from app.libs.httper import Http
from flask import current_app


class YuShuBook:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword,
                                     current_app.config["PER_PAGE"],
                                     YuShuBook.calculate_start(page))
        result = Http.get(url)
        return result

    @classmethod
    def calculate_start(cls, page):
        return (page-1) * current_app.config["PER_PAGE"]
