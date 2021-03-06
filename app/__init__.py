__author__ = "ハリネズミ"
from flask import Flask
from app.models.book import db


def create_app():
    # ここで使用してる__name__がプロジェクトの根を決めてる
    app = Flask(__name__)
    app.config.from_object("app.secure")
    app.config.from_object("app.setting")
    register_blueprint(app)

    # db.init_app(app)
    # db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
