# 插件管理
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 创建插件对象
db = SQLAlchemy()
migrate = Migrate()


# 初始化插件
def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)


