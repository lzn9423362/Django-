
from flask import Blueprint, render_template, request, Response

blue = Blueprint('blue', __name__)

@blue.route('/')
def home():
    return 'home'


@blue.route('/index/')
def index():
    user = request.cookies.get('user')
    return render_template('index.html', user=user)


@blue.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('username')
        password = request.form.get('password')
        response = Response('haha')
        response.set_cookie('user', user, max_age=6000)
        return response
