from flask_script import Manager
from app import app
# from db_script import DBManager
from flask_migrate import Migrate, MigrateCommand
from models import Article
from exts import db

manager = Manager(app)

#init初始化迁移环境
#migrate生成迁移文件
#upgrade映射到表中


#1.要使用flask_migrate，必须绑定app和db
migrate = Migrate(app, db)

#2.　把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)

# python manage.py runserver
@manager.command
def runserver():
    print('服务器跑起来了')

# manager.add_command('db', DBManager)

if __name__ == '__main__':
    manager.run()