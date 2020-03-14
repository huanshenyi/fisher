## 検索機能
キーワード
isbn


## 雑記

```python

# flaskのデコレーター == app.add_url_rule
from flask import Flask
app = Flask(__name__)
@app.route("/hello")
def hello():
    return "hello1"

app.add_url_rule("/hello", view_func=hello)
```

```python
    headers = {
        "content-type": "application/json",
        "location": "http://www.bing.com"
    }
    response = make_response("<html></html>", 200)
    response.headers = headers
    return response

    return "<html></html>", 301, headers
```

データapi
```python
http://t.yushu.im/v2/book/search?q={}&start={}&count={}

http://t.yushu.im/v2/book/isbn/{isbn}
```
