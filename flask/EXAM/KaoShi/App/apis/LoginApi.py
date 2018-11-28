from flask import redirect, session

from App.exts import db
from App.models import User
from flask_restful import Resource, fields,marshal_with,reqparse

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help='必须填写用户名')
parser.add_argument('password', type=str, required=True, help='必需填写密码')



class LoginResource(Resource):
    def post(self):
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        print(username, password)
        user = User.query.filter(User.name==username,User.passwd==password).first()
        if user:
            session['username'] = username
            return redirect('/index/')

        return {'msg':'账号密码错误'}