# 程序入口
# 命令管理
from flask_script import Manager
from flask_migrate import MigrateCommand
from App import init_app

app = init_app()
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)  # 添加命令：数据迁移


if __name__ == '__main__':
    manager.run()

