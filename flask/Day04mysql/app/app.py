from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

#onetomany
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('articles'))#backref是定义反向引用,是通过user这个模型可以访问访问这个user所写的所有文章


#manytomany
article_tag = db.Table('article_tag',
                       db.Column('article_id', db.Integer, db.ForeignKey('article1.id'),primary_key=True),
                       db.Column('tag_id', db.Integer, db.ForeignKey('tag1.id'),primary_key=True))

class Article1(db.Model):
    __tablename__ = 'article1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)

    tags = db.relationship('Tag1', secondary=article_tag, backref=db.backref('articles'))

class Tag1(db.Model):
    __tablename__ = 'tag1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

db.create_all()

@app.route('/')
def onetomany():
    #增加作者
    # user1 = User(username='zhiliao')
    # db.session.add(user1)
    # db.session.commit()
    #增加文章
    # article = Article(title='１１１', content='２２２', author_id=1)
    # db.session.add(article)
    # db.session.commit()

    #查找文章标题为aaa的作者名称
    # article = Article.query.filter(Article.title == 'aaa').first()
    # author_id = article.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print(user.username)

    #找文章标题为aaa的这个作者,正向查找
    article = Article.query.filter(Article.title == 'aaa').first()
    print(article.author.username)

    #我要找到知了这个用户写过的所有文章,反向查找
    user = User.query.filter(User.username == 'zhiliao').first()
    result = user.articles
    for article in result:
        print('*'*10)
        print(article.title)

    return 'Hello World!'

@app.route('/1/')
def manytomany():
    #添加数据
    # article1 = Article1(title='aaa')
    # article2 = Article1(title='bbb')
    #
    # tag1 = Tag1(name='111')
    # tag2 = Tag1(name='222')
    #
    # article1.tags.append(tag1)
    # article1.tags.append(tag2)
    # article2.tags.append(tag1)
    # article2.tags.append(tag2)
    #
    #
    # db.session.add(article1)
    # db.session.add(article2)
    # db.session.add(tag1)
    # db.session.add(tag2)
    #
    # db.session.commit()

    article3 = Article1.query.filter(Article1.title == 'aaa').first()
    tags = article3.tags
    for tag in tags:
        print(tag.name)
    return 'haha'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
