from flask_login import current_user, login_required

from app.forms.poem_post import PoemForm
from app.models.poetry import Poetry
from app.models.poem import Poem
from app.models.base import db
from . import web
from flask import render_template, flash, request, redirect, url_for


@web.route('/about')
def about():
    return render_template("about.html")


@web.route('/explore')
def explore():
    return render_template("explore.html")


@web.route('/poem_pub', methods=["POST", "GET"])
@login_required
def poem_pub():
    choices = Poetry.get_poetry_by_user(current_user)
    form = PoemForm(choices)
    if request.method == 'POST' and form.validate():
        poem = Poem()
        poem.set_attrs(form.data)
        poem.poetry = choices[form.poetry.data]
        poem.user = current_user
        with db.auto_commit():
            db.session.add(poem)
            poem.update_send_counter()
        flash('发布成功', category='success')
        return redirect(url_for('web.personal'))
        # return render_template('poem_pub.html', form=form)
    return render_template('poem/poem_pub.html', form=form, choices=choices)


# 自己看的诗歌界面，怎么添加下一页和上一页的访问
@web.route('/poem/<int:id>')
@login_required
def poem(id):
    poems = Poem.query.filter_by(uid=current_user.id, status=1).all()
    # now_poem = poems[id] if id<len(poems.all()) else poems.first()
    pre_poem, now_poem, next_poem = None, None, None
    for index in range(len(poems)):
        if poems[index].id == id:
            now_poem = poems[index]
            pre_poem = poems[index - 1] if index - 1 >= 0 else None
            next_poem = poems[index + 1] if index + 1 < len(poems) else None
    # now_poem = Poem.query.get(id)
    # pre_poem = Poem.query.get(id - 1)
    # next_poem = Poem.query.get(id + 1)
    return render_template('poem/poem.html', poems={'now_poem': now_poem, 'pre_poem': pre_poem, 'next_poem': next_poem})


@web.route('/poem/_del/<int:id>')
@login_required
def poem_del(id):
    tmp_poem = Poem.query.get(id)
    if current_user.id == tmp_poem.uid:
        tmp_poem.fake_del()
        flash('已移到回收站！', category='success')
    return redirect(url_for('web.personal'))
    # return
