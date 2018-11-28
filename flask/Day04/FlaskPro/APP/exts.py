from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_cache import Cache
db = SQLAlchemy()
debugtoolbar = DebugToolbarExtension()
cache = Cache(config={
    'CACHE_TYPE': 'simple'
})

def init_exts(app):
    db.init_app(app=app)
    Bootstrap(app)
    debugtoolbar.init_app(app)
    cache.init_app(app=app)
    migrate = Migrate(app=app, db=db)