from flask import Flask

from App.models import db
from App.views import init_blue


def init_app():
    app = Flask(__name__)
    DB_URI = 'sqlite:///sqlite3.db'


    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    HOSTNAME = 'localhost'
    PORT = '3306'
    DATABASE = 'flaskdb'
    USERNAME = 'root'
    PASSWORD = '0000'

    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD,
                                                                           HOSTNAME, PORT, DATABASE)


    #配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #初始化orm
    db.init_app(app=app)
    #初始化蓝图
    init_blue(app)
    return app