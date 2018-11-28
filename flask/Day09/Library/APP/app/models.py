import datetime

from app.exts import db




collection = db.Table('collection',
          db.Column('book_id', db.Integer, db.ForeignKey('book.id'),primary_key=True),
          db.Column('publisher_id', db.Integer, db.ForeignKey('publisher.id'),primary_key=True),
                      )

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    age = db.Column(db.Integer, default=10)
    sex = db.Column(db.String(20), default=0)
    email = db.Column(db.String(50))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), unique=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey('author.id'))
    author = db.relationship('Author', backref=db.backref('books'))


class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(20))
    city = db.Column(db.String(20))
    province = db.Column(db.String(20))
    country = db.Column(db.String(30))
    website = db.Column(db.String(30))
    books = db.relationship('Book',backref=db.backref('publishers'),secondary=collection)

