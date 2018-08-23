from app.models.poem import Poem
from . import web
from flask_login import login_required, current_user
from flask import render_template, flash


@web.route('/personal')
@login_required
def personal():
    # Poem
    poems = Poem.query.filter_by(uid=current_user.id, status=1).all()
    return render_template('personal.html', poems=poems)


@web.route('/user_info')
@login_required
def user_info():
    return render_template('user_info.html')
