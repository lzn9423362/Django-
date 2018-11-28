import datetime

from exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('questions'))

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    question = db.relationship('Question', backref=db.backref('answers'))


# def func(a, b=[]):
#     b.append(a)
#     print(b)
# li = [1, 1, 1, 23, 3, 4, 4]
# new_li = list(set(li))
# # new_li.sort(key=li.index)
# print(new_li)
#
#

str1 = 'first'

str1 = ','.join(str1)
print(str1)
l1 = str1.split(',')

print(l1)