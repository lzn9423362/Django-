# import uuid
#
# from flask import render_template
# from flask_mail import Message
#
# from App.exts import db, mail, cache
# from flask_restful import reqparse, Resource, fields
# from App.models import User
# parser = reqparse.RequestParser()

# parser.add_argument('username', type=str, required=True, help='不能为空')
# parser.add_argument('password', type=str, required=True, help='不能为空')
# parser.add_argument('email', type=str, required=True, help='不能为空')
#
#
# user_field = {
#     'username': fields.String,
#     'email': fields.String
# }
#
# result_field = {
#     'returnCode': fields.String,
#     'msg': fields.String,
#     'returnValue': fields.Nested(user_field),
# }

# class Register(Resource):
#     def post(self):
#         args = parser.parse_args()
#         username = args.get('username')
#         password = args.get('password')
#         email = args.get('email')
#         token = str(uuid.uuid4())
#         user = User(username=username,password=password,email=email,user_token=token)
#         try:
#             db.session.add(user)
#             db.session.commit()
#             msg = Message(subject='淘票票', sender='lzn943362@qq.com', recipients=[email])
#             msg.html = render_template('user_active.html', usenrame=username, active_url='http://192.168.154.142:5000/useractive/?token=%s'%token)
#             mail.send(msg)
#             cache.set(token, user.id, timeout=300)
#         except Exception as e:
#             return {'returnCode': -1, 'msg': str(e)}
#         return {'returnCode': '0', 'msg': 'success', 'returnValue': User.query.all()}
#
# class Login(Resource):
#     def post(self):
#         args = parser.parse_args()
#         username = args.get('username')
#         password = args.get('password')
#         user = User.query.filter(User.username == username).first()
#         if user:
#
#
