"""
    Created by ZZXUN on 2018/8/6
"""
from flask import Flask, current_app

__author__ = "ZZXUN"

app = Flask(__name__)

# ctx = app.app_context()

ctx = app.app_context()
ctx.push()  # 手动推入应用上下文，才能获取当前应用的配置
a = current_app
d = current_app.config["DEBUG"]
print(d)
ctx.pop()  # 请求结束后上下文出栈

# with 改写代码
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']
