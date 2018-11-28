from flask import g


def login_log():
    print(g.username)


