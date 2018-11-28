import random

from flask import Blueprint, render_template, request, jsonify

from APP.models import *

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blue)


@blue.route('/')
def hello():
    return render_template('index.html')

@blue.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        print(username,password,email)
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return '哈哈'



@blue.route('/registerajax/', methods=['POST', 'GET'])
def registerajax():
    if request.method == 'POST':
        username = request.form.get('user')
        print(username)
        user = User.query.filter(User.username == username).first()
        if user:
            return jsonify({'status': 2})
        else:
            return jsonify({'status': 1})
    else:
        return jsonify({'status': 0})





@blue.route('/addbanji/')
def add_banji():
    banji = Banji()
    banji.name = '1808'
    db.session.add(banji)
    db.session.commit()
    return '添加成功'

@blue.route('/addstudent/')
def add_student():
    stu = Student()
    stu.name = '崔永元' + str(random.randint(1,9))
    stu.age = random.randint(10,40)
    stu.banji = Banji.query.filter(Banji.name == '1808').first().id
    db.session.add(stu)
    db.session.commit()
    return '添加学生成功'

@blue.route('/findbanji/')
def find_banji():
    stu = Student.query.get(1)
    print(stu.banji)
    # banji = Banji.query.get(stu.banji)
    banji = stu.bj
    print(banji)
    return '查找到的学生班级是: %s'%stu.banji

@blue.route('/findstudents/')
def find_students():
    banji = Banji.query.filter(Banji.name.contains('1808')).first()
    students = banji.students
    print(students)
    return render_template('student_list.html', students=students)

@blue.route('/addusermovie/')
def add_usermovie():
    usermovie = Usermovie()
    usermovie.name = '崔永元' + str(random.randint(1, 9))
    usermovie.age = random.randint(10, 40)
    db.session.add(usermovie)
    db.session.commit()
    return '添加用户成功'

@blue.route('/addmovie/')
def add_movie():
    movie = Movie()
    movie.name = '手机' + str(random.randint(1,9))
    db.session.add(movie)
    db.session.commit()
    return '添加电影成功呢'
@blue.route('/addcollection/')
def add_collection():
    usermovie = Usermovie.query.get(1)
    movie = Movie.query.get(2)
    usermovie.movies.append(movie)
    db.session.commit()
    print(usermovie.movies)
    return '哈哈你被谁控制了'

