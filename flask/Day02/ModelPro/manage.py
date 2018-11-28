from flask import Flask
from flask_script import Manager

from App import init_app




app = init_app()

manage = Manager(app=app)


if __name__ == '__main__':
    manage.run()
