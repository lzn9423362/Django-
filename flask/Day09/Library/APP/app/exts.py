from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def init_exts(app):
    db.init_app(app)
    migrate = Migrate(app=app, db=db)