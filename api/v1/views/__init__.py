#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/')

from api.v1.views.index import *
from api.v1.views.course import *
from api.v1.views.enrollment import *
from api.v1.views.lesson import *
from api.v1.views.quiz import *
from api.v1.views.review import *
from api.v1.views.users import *
from api.v1.views.category import *
