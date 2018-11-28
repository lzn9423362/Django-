from App.models import *
from flask_restful import Resource, fields, marshal_with, marshal


# 资源
class Home(Resource):
    def get(self):
        return {'get': "强东"}

    def post(self):
        return {'post': "抹茶妹妹"}



city_fields = {
    'id': fields.Integer,
    'parentId': fields.Integer,
    'regionName': fields.String,
    'cityCode': fields.Integer,
    'pinYin': fields.String,
}


letter_fields = {

    'A': fields.List(fields.Nested(city_fields)),
    'B': fields.List(fields.Nested(city_fields)),
    'C': fields.List(fields.Nested(city_fields)),
    'D': fields.List(fields.Nested(city_fields)),
    'E': fields.List(fields.Nested(city_fields)),
    'F': fields.List(fields.Nested(city_fields)),
    'G': fields.List(fields.Nested(city_fields)),
    'H': fields.List(fields.Nested(city_fields)),
    'I': fields.List(fields.Nested(city_fields)),
    'J': fields.List(fields.Nested(city_fields)),
    'K': fields.List(fields.Nested(city_fields)),
    'L': fields.List(fields.Nested(city_fields)),
    'M': fields.List(fields.Nested(city_fields)),
    'N': fields.List(fields.Nested(city_fields)),
    'O': fields.List(fields.Nested(city_fields)),
    'P': fields.List(fields.Nested(city_fields)),
    'Q': fields.List(fields.Nested(city_fields)),
    'R': fields.List(fields.Nested(city_fields)),
    'S': fields.List(fields.Nested(city_fields)),
    'T': fields.List(fields.Nested(city_fields)),
    'U': fields.List(fields.Nested(city_fields)),
    'V': fields.List(fields.Nested(city_fields)),
    'W': fields.List(fields.Nested(city_fields)),
    'X': fields.List(fields.Nested(city_fields)),
    'Y': fields.List(fields.Nested(city_fields)),
    'Z': fields.List(fields.Nested(city_fields)),
}

#处理返回字段
result_fields = {
    'returnCode' : fields.String,
    'returnValue': fields.Nested(letter_fields)
}

class CityResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        city_letters = CityLetter.query.all()
        return_value = {}
        for city_letter in city_letters:
            citys = city_letter.citys #每个字母包含的所有城市列表
            return_value[city_letter.letter] = citys

        data = {
            "returnCode": '0',
            "returnValue": return_value,
        }
        return data

    # def post(self):
    #     city_letters = CityLetter.query.all()
    #     return_value = {}
    #     letter_fields_dynamic = {}
    #     for city_letter in city_letters:
    #         citys = city_letter.citys  # 每个字母包含的所有城市列表
    #         return_value[city_letter.letter] = citys
    #         letter_fields_dynamic[city_letter.letter] = fields.List(fields.Nested(city_fields))
    #     result_fields_dynamic = {
    #         "returnCode": fields.String,
    #         "returnValue": fields.Nested(letter_fields_dynamic),
    #     }
    #     data = {
    #         "returnCode": '0',
    #         "returnValue": return_value,
    #     }
    #     return marshal(data, result_fields_dynamic)

    def post(self):
        city_letters = CityLetter.query.all()
        return_value = {}
        letter_fields_dynamic = {}
        for city_letter in city_letters:
            citys = city_letter.citys
            return_value[city_letter.letter] = citys
            letter_fields_dynamic[city_letter.letter] = fields.List(fields.Nested(city_fields))
            result_fields_dynamic = {
                'returnCode': fields.String,
                'returnValue': fields.Nested(letter_fields_dynamic)
            }
            data = {
                'returnCode': 0,
                'returnValue': return_value
            }
            return marshal(data, result_fields_dynamic)
# {
#   "returnCode": "0",
#   "returnValue": {
#     "A": [
#       {
#         "id": 3643,
#         "parentId": 0,
#         "regionName": "阿坝",
#         "cityCode": 513200,
#         "pinYin": "ABA"
#       },