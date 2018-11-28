# 配置数据库
# sqlite
# DB_URI = "sqlite:///sqlite3.db"
# mysql
# DB_URI = "mysql+pymysql://root:root@127.0.0.1:3306/db"
#
# # 配置数据库
# app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
# # 禁止对象追踪修改
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


import os

# BASE_DIR: 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#
def db_uri(database):
    db = database.get('DB')
    driver = database.get('DRIVER')
    user = database.get('USER')
    password = database.get('PASSWORD')
    host = database.get('HOST')
    port = database.get('PORT')
    name = database.get('NAME')

    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


# 配置
class Config(object):
    DEBUG = False

    # 禁止对象追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '111'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = 'lzn943362@163.com' #用户名
    MAIL_PASSWORD = 'lzn943362' #授权码



# 开发环境
class DevelopConfig(Config):
    # 开启调试模式
    DEBUG = True
    ENV = 'delevelopment'
    RESTFUL_JSON = dict(ensure_ascii=False)
    # 数据库配置
    DATABASE = {
        'DB': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '0000',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'tpp',
    }
    SQLALCHEMY_DATABASE_URI = db_uri(DATABASE)


# 生产环境
class ProductConfig(Config):
    # 关闭调试模式
    DEBUG = False
    ENV = 'production'

    # 数据库配置
    DATABASE = {
        'DB': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '0000',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'tpp',
    }
    SQLALCHEMY_DATABASE_URI = db_uri(DATABASE)


env = {
    'development': DevelopConfig,  # 开发环境
    'production': ProductConfig,  # 生产环境
}
