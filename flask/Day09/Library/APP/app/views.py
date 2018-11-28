from flask import Blueprint, render_template
from .models import *
blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blue)




@blue.route('/bookindex/')
def book_index():
    return render_template('book_index.html')

@blue.route('/booklist/')
def book_list():
    books = Book.query.all()
    return render_template('book_list.html', books=books)

@blue.route('/bookdetail/<id>/')
def book_detail(id):
    book = Book.query.get(id)
    publishers = book.publishers
    author = book.author
    return render_template('book_detail.html',book=book, publishers=publishers, author=author)

@blue.route('/authordetail/<id>/')
def author_detail(id):
    author = Author.query.get(id)
    return render_template('author_detail.html',author=author)

@blue.route('/publisherdetail/<id>/')
def publisher_detail(id):
    publisher = Publisher.query.get(id)
    return render_template('publisher_detail.html', publisher=publisher)