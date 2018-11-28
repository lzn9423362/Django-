from flask_restful import Resource, reqparse, abort
from App.models import User

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='未知用户')

#

def check_permission(permission):
    def outer(func):
        def inner(*arg, **kwargs):
            args = parser.parse_args()
            token = args.get('token')
            user = User.query.filter_by(user_token=token).first()
            if user:
                user_permission = user.permission

                if permission & user_permission == permission:
                   return func(*arg, **kwargs)
                else:
                    abort(403, message='权限不足')
            else:
                abort(401, message='请先登录')
        return inner
    return outer


class PermissionResource(Resource):
    #假设当前功能需要有０１００权限
    @check_permission(4)
    def get(self):
        return {'msg': '可以免广告'}
    @check_permission(8)
    def post(self):
        return {'msg': '可以下载电影'}
