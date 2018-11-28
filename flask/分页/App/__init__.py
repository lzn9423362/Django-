from flask import Flask

from App.exts import init_exts
from App.views import init_blue


def init_app():
    app = Flask(__name__)

    # sqlite
    # DB_URI = "sqlite:///sqlite3.db"
    # mysql
    DB_URI = "mysql+pymysql://root:root@127.0.0.1:3306/flaskdb"

    # 配置数据库
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 禁止对象追踪修改


    # 初始化插件
    init_exts(app)

    # 初始化蓝图
    init_blue(app)

    return app


