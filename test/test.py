from flask import Flask, current_app

app = Flask(__name__)

# app-context
# Request-context
# Flask AppContext
# Request RequestContext
# ユニットテスト
ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config["DEBUG"]
ctx.pop()

# with
with app.app_context():
    a = current_app
    d = current_app.config["DEBUG"]

# contextプロトコール出来てるオブジェクトにwithを使える
#  contextプロトコール === __enter__ && __exit__ を定義


class MyResource:
    def __enter__(self):
        print("connect to resource")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        # エラーの処理用
        # もし__exit__に入ってエラーがなければ
        # exc_type, exc_value, tb == None
        # exc_value == エラーの原因
        if tb:
            print("process exception")
        else:
            print("no exception")
        print("close resource connection")
        # __exit__ の return のValue は True or False
        # if Value == False 、関数実行後にまたエラーが出る
        return True

    def query(self):
        print("query data")

try:
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as ex:
    print("return Falseの場合")
    pass


# with open("") as f:

