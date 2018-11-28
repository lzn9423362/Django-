import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.urandom(24)
DEBUG = True

DIALECT = 'mysql'
DRIVER = 'pymysql'
HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'flaskuse'
USERNAME = 'root'
PASSWORD = '0000'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

