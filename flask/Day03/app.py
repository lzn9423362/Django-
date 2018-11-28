from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)

db.create_all()


@app.route('/1')
def mysql1():
    # 1.增
    # article1 = Article(title='a1')
    # db.session.add(article1)
    # db.session.commit()

    # 2.查
    # art = Article.query.filter(Article.id == 4).first()
    # print(art.title)

    #3.改
    # article1 = Article.query.filter(Article.id == 2).first()
    # article1.title = 'a2'
    # db.session.commit()

    #4.删
    # article1 = Article.query.filter(Article.id == 3).first()
    # db.session.delete(article1)
    # db.session.commit()

    return 'Hello world'

#反向解析
@app.route('/')
def hello_world():
    print(url_for('my_list'))
    print(url_for('article', id='1'))
    return redirect(url_for('article',id=1))

@app.route('/article/<id>')
def article(id):
    return '你请求的参数是%s' % id

@app.route('/list/')
def my_list():
    return 'list'

@app.route('/index')
def index():
    context = {
        'username': '治疗课堂',
        'username1': '治疗',
        'username2': '治疗课',
    }
    return render_template('index.html', **context, username3=1)



if __name__ == '__main__':
    app.run()
