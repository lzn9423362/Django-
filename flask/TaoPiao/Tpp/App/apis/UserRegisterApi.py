import uuid

from flask import render_template
from flask_mail import Message

from App.models import User
from flask_restful import Resource, fields, marshal_with,reqparse
from App.exts import db, mail, cache
from werkzeug.security import generate_password_hash
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='必须填写用户名')
parser.add_argument('password', type=str, required=True, help='必须填写密码')
parser.add_argument('email', type=str, required=True, help='必须填写邮箱')

user_fields = {
    'username': fields.String,
    'email': fields.String
}

result_fields = {
    'returnCode': fields.String,
    'msg': fields.String,
    'returnValue': fields.Nested(user_fields)
}


class Register(Resource):
    @marshal_with(result_fields)
    def post(self):
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        email = args.get('email')

        #注册(添加用户数据)
        usertoken = str(uuid.uuid4())
        user = User(username=username, password=generate_password_hash(password), email=email, user_token=usertoken)
        try:
            db.session.add(user)
            db.session.commit()

            #发送邮件激活用户
            msg = Message(subject='淘票票用户激活', sender='lzn943362@163.com', recipients=[email])
            #邮件内容
            # msg.html = '<b>hello 淘票票</b>'
            msg.html = render_template('user_active.html', username=username, active_url='http://39.108.52.181/active/?token=%s' %user.user_token)
            mail.send(msg)
            cache.set(usertoken, user.id, timeout=300)
        except Exception as e:
            return {'returnCode': '-1', 'msg': str(e)}
        return {'returnCode': '0', 'msg': 'success', 'returnValue': User.query.all()}


