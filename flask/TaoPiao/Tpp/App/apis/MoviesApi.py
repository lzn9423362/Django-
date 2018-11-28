from flask_restful import Resource, fields, marshal_with,reqparse

from App.models import Movies

parser = reqparse.RequestParser()
#flag １表示正在热映，２表示即将上映
parser.add_argument('flag', type=int, default=1)

movie_fields = {
    'id': fields.Integer,
    'showname': fields.String,
    'shownameen': fields.String,
    'director': fields.String,
    'leadingRole': fields.String,
    'country': fields.String,
    'language': fields.String,
    'duration': fields.Integer,
    'screeningmodel': fields.String,
    'openday': fields.DateTime,
    'backgroundpicture': fields.String,
}


result_fields = {
    'movies': fields.List(fields.Nested(movie_fields))
}


class MoviesResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        args = parser.parse_args()
        flag = args.get('flag')
        movies = Movies.query.filter(Movies.flag == flag)

        data = {
            'movies': movies
        }
        return data