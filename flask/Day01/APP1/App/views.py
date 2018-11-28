import uuid

from flask import Blueprint, request, render_template, make_response, abort
#创建蓝图对象，规划路由
blue = Blueprint('first', __name__)

# @blue.route('/')
# def index():
#     return 'haha'


@blue.route('/getstudent/<id>/')
def get_student(id):
    print(id)
    print(type(id))
    return 'haha'

@blue.route('/getstudent1/<int:id>')
def get_student1(id):
    print(id)
    print(type(id))
    return 'get_person: %dls' %id

#任意一个，要为ａｎｙ中的任意一个
@blue.route('/getany/<any(movie,music,code):like>')
def get_any(like):
    print(like)
    return like



print(uuid.uuid4())
@blue.route('/getuuid/<uuid:uid>/')
def get_uuid(uid):
    print(uid)
    print(type(uid))
    uid = str(uid)
    return uid


@blue.route('/request/', methods=['POST', 'GET'])
def make_request():
    print(request)
    print(request.url)
    print(request.base_url)
    print(request.host_url)
    print(request.path)

    return 'haha'


@blue.route('/response/', methods=['POST', 'GET'])
def set_response():
    response = make_response('<b>陳學兵</b>')
    print(response)#<Response 16 bytes [200 OK]>
    print(type(response))
    return response

@blue.route('/response1/')
def response1():
    return render_template('response.html', name='哈哈')

#终止程序,抛出异常
@blue.route('/abort/')
def make_abort():
    abort(502)
    return 'abort'

@blue.errorhandler(502)
def error_handler(e):
    print(e)
    return '123'

