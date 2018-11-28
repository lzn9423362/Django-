import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRETE_KEY = os.urandom(24)


class DevelopConfig(Config):
    DEEBUG = True
    DATABASE = {

    }