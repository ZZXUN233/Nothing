"""
    Created by ZZXUN on 2018/8/6
"""
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from app.forms.auth import RegisterForm, LoginForm, ChangePwdForm, InfoForm, EmailForm, ResetPasswordForm
from app.models.base import db
from app.models.user import User
from app.models.poetry import Poetry
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
        # if not form.password.data == form.password_again.data:
        #     flash('两次密码不匹配！', category='warning')
        #     return render_template("auth/register.html", form=form)
        user = User()
        # Poetry
        user.set_attrs(form.data)  # 对象传值
        with db.auto_commit():
            db.session.add(user)
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
            flash("登录成功！", category='success')
            if not Poetry.query.filter_by(user=user).first():
                Poetry.default_poetry(user)
            if not next_step or not next_step.startswith('/'):
                next_step = url_for('web.index')
            return redirect(next_step)
        else:
            flash('用户不存在或密码错误！', category='warning')
    return render_template("auth/login.html", form=form)


@web.route('/logout')
@login_required
def logout():
    logout_user()
    flash("你已退出登录！", category='success')
    return redirect(url_for('web.index'))


@web.route('/forget_pwd', methods=['POST', 'GET'])
def forget_pwd():
    form = EmailForm(request.form)
    if request.method == "POST":
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            from app.libs.email import send_mail
            send_mail(form.email.data, '重置你的密码',
                      'email/reset_password.html', user=user,
                      token=user.generate_token())
            flash('一封邮件已经发送至你的邮箱' + account_email + '，请注意查收！', category='success')
            return render_template('auth/login.html', form=form)
            # return redirect(url_for('web.login'))
    return render_template('auth/forgot.html')


@web.route('/reset/password/<token>', methods=['POST', 'GET'])
def reset_pwd(token):
    if not current_user.is_anonymous:
        print('用户不存在！')
        return redirect(url_for('web.index'))
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        result = User.reset_password(token, form.new_password.data)
        if result:
            flash('你的密码已经更新，请使用新密码登录', category='success')
            return redirect(url_for('web.login', form=form))
        else:
            return redirect(url_for('web.index'))
    return render_template('auth/reset_pwd.html')


@web.route('/change_pwd', methods=["POST", "GET"])
@login_required
def change_pwd():
    form = ChangePwdForm(request.form)
    if request.method == 'POST' and form.validate():
        current_user.change_pwd(form.old_password.data, form.new_password2.data)
        with db.auto_commit():
            db.session.add(current_user)
            flash("密码已成功修改！", category='success')
        return redirect(url_for('web.user_info'))
    return render_template("auth/change_pwd.html")


@web.route('/change_info', methods=['POST', 'GET'])
# @login_required
def change_info():
    form = InfoForm()
    if request.method == 'POST' and form.validate():
        info_dict = {
            'nickname': form.new_nickname.data,
            'phone_number': form.phone_number.data,
            'new_email': form.new_email.data
        }
        current_user.change_info(info_dict)
        with db.auto_commit():
            db.session.add(current_user)
        flash('修改成功！', category='success')
        return redirect(url_for('web.user_info'))
    return render_template('user_info.html', form=form)
