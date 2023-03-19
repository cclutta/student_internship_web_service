#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.users import *
from api.v1.views.students import *
from api.v1.views.lecturers import *
from api.v1.views.internships import *