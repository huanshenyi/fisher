__author__ = "ハリネズミ"
from sqlalchemy import Column, Integer, String


# sqlalchemy
class Book():
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default="匿名")
    binding = Column(String(20))   # 規格?一般、特殊
    publisher = Column(String(50)) # 出版社
    price = Column(String(30))
    pages = Column(Integer)
    pubdate = Column(String(20))   # 出版日
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000)) # 紹介
    image = Column(String(50))

