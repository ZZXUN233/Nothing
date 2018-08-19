from flask import render_template
from datetime import datetime

from . import web


@web.route('/')
@web.route('/index')
def index():
    # flash("hello world!", category="hello")  # 消息闪现
    # flash("hello zzx", category="zzx")
    return render_template("index.html", current_time=datetime.utcnow())


@web.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@web.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
