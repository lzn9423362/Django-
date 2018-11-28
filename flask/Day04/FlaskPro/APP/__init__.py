from flask import Flask

from APP import config
from APP.exts import init_exts
from APP.views import init_blue


def init_app():
    app = Flask(__name__)
    app.config.from_object(config)
    init_blue(app)
    init_exts(app)
    return app
