from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
api = Api()

def init_exts(app):
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
