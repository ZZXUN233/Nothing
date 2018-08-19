"""
    Created by ZZXUN on 2018/8/6
"""
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web

__author__ = "ZZXUN"


@web.route('/register', methods=['GET', 'POST'])
def register():
    """
    1.返回注册页面 get
    2.处理注册页面的请求 post
    :return:
    """
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        if not form.password.data == form.password_again.data:
            flash('两次密码不匹配！')
            return render_template("auth/register.html", form=form)
        user = User()
        user.set_attrs(form.data)  # 对象传值
        db.session.add(user)
        db.session.commit()
        # 页面重定向
        # return redirect(url_for('web.login', form=form))
        return render_template("auth/login.html", form=form)
    return render_template("auth/register.html", form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            # 登录成功后写入cookie，用户票据信息写入cookie
            # login_user(user, remember=True)
            login_user(user)
            next_step = request.args.get('next')
            flash("登录成功！")
            if not next_step or not next_step.startswith('/'):
                next_step = url_for('web.index')
            return redirect(next_step)
        else:
            flash('用户不存在或密码错误！')
    return render_template("auth/login.html", form=form)


@web.route('/logout')
@login_required
def logout():
    logout_user()
    flash("你已退出登录！")
    return redirect(url_for('web.index'))


@web.route('/reset')
def reset():
    return render_template("auth/reset.html")
