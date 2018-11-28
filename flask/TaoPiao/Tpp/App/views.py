from flask import Blueprint, render_template, request

blue = Blueprint('blue', __name__)
def init_blue(app):
    app.register_blueprint(blue)

@blue.route('/index/')
def index():
    return render_template('index.html')


@blue.route('/movielist/')
def movie_list():
    return render_template('movies.html')

@blue.route('/redister/', methods=['GET', 'POST'])
def redister():
    if request.method == 'GET':
        return render_template('redister.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        print(username,password,email)
        return '哈哈'