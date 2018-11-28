from flask import Blueprint, render_template, session, request, redirect

from App.exts import db
from App.models import User

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blue)

@blue.route('/index/')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)



@blue.route('/register/', methods=['GET', 'POST'])
def register():
        return render_template('register.html')


@blue.route('/login/')
def login():
    return render_template('login.html')

@blue.route('/logout/')
def logout():
    session.clear()
    return redirect('/index/')
