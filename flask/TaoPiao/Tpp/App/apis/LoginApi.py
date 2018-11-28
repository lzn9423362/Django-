from flask import request, session
from werkzeug.security import check_password_hash

from App.models import *
from flask_restful import Resource, reqparse, fields, marshal_with

parse = reqparse.RequestParser()
parse.add_argument('username', required=True, type=str, help='必须填写用户名')
parse.add_argument('password', required=True, type=str, help='必须填写用户名')


user_fields ={
    'username': fields.String,
    'useremail': fields.String(attribute='email'),
    'usertoken': fields.String(attribute='user_token')
}
result_fields = {
    'msg': fields.String,
    'data': fields.Nested(user_fields)
}

class Login(Resource):
    @marshal_with(result_fields)
    def post(self):
        args = parse.parse_args()
        username = args.get('username')
        password = args.get('password')
        user = User.query.filter(User.username == username).first()
        data = {
            "returnCode": '0',
            'msg': 'error',
        }
        if user:
           if check_password_hash(user.password, password):
               if user.is_active:
                session['username'] = username
                data['msg'] = 'success'
                data['data'] = user

        return data