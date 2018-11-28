from flask import Flask

from app import config
from app.exts import init_exts
from app.views import init_blue


def init_app():
    app = Flask(__name__)
    init_blue(app)
    app.config.from_object(config)
    init_exts(app)
    return app
