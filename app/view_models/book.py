__author__ = "ハリネズミ"


class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        """
        単一のデータを返す場合の整形
        :param data: spiderから取得した元データ
        :param keyword: 検索キーワード
        :return:
        """
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned["total"] = 1
            returned["books"] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        """
        複数のデータを返す場合の整形
        :param data: spiderから取得した元データ
        :param keyword: 検索キーワード
        :return:
        """
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned["total"] = data["total"]
            returned["books"] = [cls.__cut_book_data(book) for book in data["books"]]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        """
        元データ解析用
        :return:
        """
        book = {
            "title": data["title"],
            "publisher": data["publisher"],
            "pages":  data["pages"] if data["pages"] else "",
            "author": "、".join(data["author"]), # 作者複数いる場合の処理
            "price": data["summary"],
            "summary": data["summary"] if data["summary"] else "",
            "image": data["image"]
        }
        return book
