from flask import session

from App.models import Banner
from flask_restful import Resource, fields,marshal_with






banner_field = {
    'img': fields.String
}


result_fields = {
    'banners': fields.List(fields.Nested(banner_field))
}
# 资源
class BannerResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        banners = Banner.query.all()
        print(banners)
        data = {
            'banners': banners
        }
        return data