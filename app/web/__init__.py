"""
    Created by ZZXUN on 2018/8/6
"""
from flask import Blueprint

__author__ = "ZZXUN"
web = Blueprint('web', __name__)

from app.web import user
from app.web import poem
from app.web import personal
from app.web import main
from app.web import graph
from app.web import author
from app.web import poetry
