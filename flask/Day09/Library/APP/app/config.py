



DIALECT = 'mysql'
DRIVER = 'pymysql'
HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'flask_library'
USERNAME = 'root'
PASSWORD = '0000'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

