from flask_restful import fields, Resource, reqparse
from App.models import User
from App.exts import db, cache

parser = reqparse.RequestParser()
parser.add_argument('token', type=str)

class UserActiveResource(Resource):
    def get(self):
        args = parser.parse_args()
        token = args.get('token')
        userid = cache.get(token)
        if userid:
            users = User.query.filter_by(user_token=token)
            if users.count() > 0:
                user = users.first()
                user.is_active = True
                db.session.add(user)
                db.session.commit()
                return {'msg': '激活成功'}
            else:
                return {'msg':'用户不存在'}
        else:
            return {'msg': '激活超时'}