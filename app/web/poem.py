from . import web
from flask import render_template, flash


@web.route('/about')
def about():
    return render_template("about.html")


@web.route('/explore')
def explore():
    return render_template("explore.html")
