from flask_script import Manager
from flask_migrate import MigrateCommand
from APP.models import *
from APP import init_app

app = init_app()
manage = Manager(app)
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()