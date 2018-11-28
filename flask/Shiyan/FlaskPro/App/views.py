from flask import Blueprint
from App.models import *


# 创建蓝图并初始化
blue = Blueprint('blue', __name__)
def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def home():
    persons = Person.query
    print(persons)
    print(type(persons))
    print(persons.get(1))
    return "Home"





