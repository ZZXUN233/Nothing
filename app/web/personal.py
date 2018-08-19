from . import web
from flask_login import login_required, current_user
from flask import render_template, flash


@web.route('/personal')
@login_required
def personal():
    return render_template('personal.html')
