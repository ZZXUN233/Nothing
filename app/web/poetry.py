from flask import request, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.models.base import db
from app.models.poetry import Poetry
from app.forms.poem_post import PoetryForm
from . import web


@web.route('/create_poetry', methods=['POST'])
@login_required
def create_poetry():
    form = PoetryForm(request.form)
    if request.method == 'POST' and form.validate():
        new_poetry = Poetry()
        new_poetry.name = form.name.data
        new_poetry.information = form.info.data
        new_poetry.user = current_user
        with db.auto_commit():
            db.session.add(new_poetry)
            print('创建成功！')
        flash('创建成功！', category='success')
        return redirect(url_for('web.personal'))
    return render_template('personal.html')
