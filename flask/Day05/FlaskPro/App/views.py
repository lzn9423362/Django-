from flask import Blueprint, jsonify, request
from flask_restful import Resource, fields, marshal_with, reqparse
from App.models import *



# 创建蓝图并初始化
blue = Blueprint('blue', __name__)
def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/1/')
def home():
    data = {
        'status': 1,
        'msg': '错误'
    }

    return jsonify(data)


@blue.route('/person/', methods=['POST', 'GET', 'PUT', 'DELETE'])
def person():
    if request.method == 'GET':
        page = int(request.args.get('page'))
        per_gage = 2
        persons = Person.query.paginate(page,per_gage,False).items
        person_dit = []
        for person in persons:
            dic = {'name': person.name}
            person_dit.append(dic)
            data = {
                'status': 1,
                'msg': 'success',
                'data': person_dit,
            }
        return jsonify(data)
    elif request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        data = {
            'status': 1,
            'msg': 'success',
        }

        if name:
            person = Person(name=name, pwd=pwd)

            try:
                db.session.add(person)
                db.session.commit()
            except:
                data['status'] = 0
                data['msg'] = '创建失败'
        else:
            data['status'] = -1
            data['msg'] = '用户名或者密码不能为空'
        return jsonify(data)
    elif request.method == 'PUT':
        name = request.form.get('name')
        old_pwd = request.form.get('oldpwd')
        new_pwd = request.form.get('newpwd')
        data = {
            'status': 1,
            'msg': 'success',
        }
        persons = Person.query.filter(Person.name == name, Person.pwd == old_pwd)
        if persons.count() > 0:
            person = persons.first()
            person.pwd = new_pwd
            db.session.commit()
        else:
            data['status'] = 0
            data['msg'] = '原用户名错误'
        return jsonify(data)
    elif request.method == 'DELETE':
        name = request.form.get('name')
        persons = Person.query.filter_by(name=name)
        data = {
            'status': 1,
            'msg': 'success',
        }
        if persons.count() > 0:
            person = persons.first()
            db.session.delete(person)
            db.session.commit()
        else:
            data['status'] = 0
            data['msg'] = '用户名不存在'
        return jsonify(data)

#资源

class Home(Resource):
    def get(self):
        return {'name': '强东'}

#给返回的数据进行过滤
person_fields = {'status': fields.Integer,
        'code': fields.Integer(default=10), #没有的字段会使用默认值
                 'msg': fields.String,
                 'data1': fields.String(attribute='private_data')
}

class PersonsResource(Resource):

    #使用person_field给get请求格式化数据
    @marshal_with(person_fields)
    def get(self):
        data = {
            'status': 1,
            'msg': 'success',
            'data': '数据',
            'private_data': '123',
        }
        return data

person_model_fields = {
    'id': fields.Integer,
    'name': fields.String,
    # 'pwd': fields.String,
    #endpoint='id',反向解析
    'url': fields.Url(endpoint='id',absolute=True),#表示当前页面的绝对路径
}

person2_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(person_model_fields), #
}


class Person2Resource(Resource):
    @marshal_with(person2_fields)
    def get(self):
        person = Person.query.first()
        data = {
            'status': 1,
            'msg': 'success',
            'data': person,
        }
        return data


person3_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(person_model_fields)), #
}

class Person3Resource(Resource):
    @marshal_with(person3_fields)
    def get(self):
        persons = Person.query.all()
        data = {
            'status': 1,
            'msg': 'success',
            'data': persons,
        }
        return data



#请求提交的参数进行解析
#type=str:会转换成制定类型
#required = True:必须参数
#help='请提交name　错误提示
#dest = 'b'起别名
#action = 'append'追加：可以有多个相同的like,最终会得到一个列表
# location:
    # location=form:

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True,help='please put your name in your face')
parser.add_argument('age', type=int, dest='bge')
parser.add_argument('like', type=str, action='append')
parser.add_argument('fldt_activ', type=str, location='cookies')

class Person4Resource(Resource):
    def get(self):
        parse = parser.parse_args()
        name = parse.get('name')
        age = parse.get('bge')
        like = parse.get('like')
        cookies = parse.get('fldt_active')
        return {'name': name, 'age': age, 'like': like, 'cookies': cookies}