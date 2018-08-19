"""
    Created by ZZXUN on 2018/8/6
"""
from flask import Flask
from flask_login import LoginManager
from app.models.base import db
from flask_bootstrap import Bootstrap
from flask_moment import Moment

__author__ = "ZZXUN"

login_manger = LoginManager()


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    moment = Moment(app)
    app.config.from_object("app.config")
    app.config.from_object("app.secure")
    register_blueprint(app)  # 加载蓝图

    db.init_app(app)
    # 初始化登陆管理插件
    login_manger.init_app(app)
    login_manger.login_view = 'web.login'
    login_manger.login_message = '请先登录或注册'
    with app.app_context():  # 核心对象入栈
        db.create_all()
    return app


# 注册蓝图
def register_blueprint(app):
    from app.web.poem import web
    app.register_blueprint(web)
