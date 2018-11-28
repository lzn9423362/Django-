from flask import Flask

from APP import config
from APP.exts import *
from .views import init_blue

def init_app():
    app = Flask(__name__)
    app.config.from_object(config)
    init_exts(app)
    init_blue(app)

    return app