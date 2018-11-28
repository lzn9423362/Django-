from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import config
from exts import db
from models import User
from md5password import my_md5

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
@app.route('/')
def index():

    return render_template('index.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == my_md5(password)).first()
        if user:
            session['telephone'] = telephone
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '账号密码错误'

@app.route('/regist/', methods=['POST', 'GET'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telepthone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(telephone=telepthone, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

@app.route('/phoneajax/', methods=['POST'])
def phoneajax():
    phone = request.form.get('phone')
    user = User.query.filter(User.telephone == phone).first()
    if user:
        return jsonify({'status': 0})
    else:
        return jsonify({'status': 1})


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/question/', methods=['POST', 'GET'])
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        pass


@app.context_processor
def my_context_processor():
    tel = session.get('telephone', '')
    user = User.query.filter(User.telephone == tel).first()
    if user:
        return {'user': user}
    else:
        return {'user': ''}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
