from flask_restful import Resource, fields, marshal_with,reqparse
from App.models import Cinemas
parser = reqparse.RequestParser()
parser.add_argument('city', type=str, default='深圳')
parser.add_argument('district', type=str, default='全部区域')
parser.add_argument('sort', type=int, default=1)

cinema_fields = {

    'name': fields.String,
    'city': fields.String,
    'district': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'score': fields.Float,
    'hallnum': fields.Integer,
    'servicecharge': fields.Integer,
    'astrict': fields.Integer
}










result_fields = {
    'cinemas': fields.List(fields.Nested(cinema_fields))
}

class CinemasResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        args = parser.parse_args()
        city = args.get('city')
        print(city)
        district = args.get('district')
        sort = args.get('sort')
        cinemas = Cinemas.query.filter(Cinemas.city == city)

        if district != '全部区域':
            cinemas.filter(Cinemas.district == district)
        if sort == 2: #评分降序
            cinemas = cinemas.order_by('-score')
        elif sort == 3:
            cinemas = cinemas.order_by('score')

        data = {
            'cinemas': cinemas
        }
        return data