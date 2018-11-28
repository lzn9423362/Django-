import time

from flask import Blueprint, render_template

from APP.exts import cache
from .models import *
blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blue)



@blue.route('/')
def home():
    return render_template('index.html')

@blue.route('/getcache/')
@cache.cached(timeout=10)
def get_cache():
    time.sleep(3)

    return render_template('index.html')