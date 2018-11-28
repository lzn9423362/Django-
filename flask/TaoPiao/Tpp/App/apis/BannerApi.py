from flask_restful import Resource, fields, marshal_with
from App.models import Banner


banner_fields = {
    'img': fields.String
}

result_fields = {
    'banners': fields.List(fields.Nested(banner_fields))
}

class BannerResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        banners = Banner.query.all()
        data = {
            'banners': banners
        }
        return data