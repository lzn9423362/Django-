

from App.models import Goods
from flask_restful import Resource, fields,marshal_with





banner_field = {
    'name': fields.String,
    'price': fields.Integer,
    'headImg': fields.String
}


result_fields = {
    'goods': fields.List(fields.Nested(banner_field))
}
# 资源
class GoodsResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        goods = Goods.query.all()

        data = {
            'goods': goods
        }
        return data