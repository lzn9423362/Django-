from flask import redirect

from App.exts import db
from App.models import User
from flask_restful import Resource, fields,marshal_with,reqparse

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help='必须填写用户名')
parser.add_argument('password', type=str, required=True, help='必需填写密码')
parser.add_argument('passwd', type=str, required=True, help='必需填写密码')



class RegisterResource(Resource):
    def post(self):
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        passwd = args.get('passwd')
        if password==passwd:
            user = User(name=username,passwd=password)
            try:
                db.session.add(user)
                db.session.commit()
                return redirect('/login/')
            except Exception as e:
                return {'msg': str(e)}

        else:
            return {'msg': '两次密码不一致'}