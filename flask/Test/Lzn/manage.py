from flask_migrate import MigrateCommand
from flask_script import Manager
from APP import init_app
# from APP.models import *
app = init_app()

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
