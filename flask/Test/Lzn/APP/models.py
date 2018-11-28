from APP.exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50),nullable=False)


# coding:utf-8




class User_food(db.Model):
    __tablename__ = 'userfood'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50),nullable=False)



class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), unique=True)
    age = db.Column(db.Integer)


class Banji(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), unique=True)
    #和Student模型建立关系，不是字段.
    #参数１　关联的　模型名称
    #２　反向查找的名称
    #　懒加载
    students = db.relationship('Student', backref='bj', lazy=True)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), unique=True)
    age = db.Column(db.String(16), default=1)
    banji = db.Column(db.Integer,db.ForeignKey(Banji.id))





collection = db.Table('collection',
                      db.Column('usermovie_id', db.Integer, db.ForeignKey('usermovie.id'), primary_key=True),
                      db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
                      )


class Usermovie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), unique=True)
    age = db.Column(db.String(16), default=1)
    movies = db.relationship('Movie', backref='usermovies', lazy=True, secondary=collection)




class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), unique=True)

