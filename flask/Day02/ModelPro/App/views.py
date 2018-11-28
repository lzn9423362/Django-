import random
import math
from flask import Blueprint, request, render_template
from App.models import *

blue = Blueprint('blue', __name__)

def init_blue(app):
  app.register_blueprint(blue)


@blue.route('/')
def home():
    return 'home'


@blue.route('/createdb/')
def create_db():
    db.create_all()
    return '创建成功'

@blue.route('/addperson/')
def add_person():
    p = Person()
    p.name = '方冰冰' + str(random.randint(10,99))
    p.age = random.randint(10,99)
    try:
        db.session.add(p)
        db.session.commit()
    except:
        db.session.rollback()
        db.session.flush()
    return '添加Person成功'


@blue.route('/addpersons/')
def add_persons():
    persons = []
    for i in range(100,110):
        p = Person(name='李晨'+str(random.randint(10,99)), age=random.randint(10,99))
        persons.append(p)

    db.session.add_all(persons)
    db.session.commit()
    return '成功'

@blue.route('/sort/<id>/')
def sortperson(id):
    page_num = 3
    page_id = int(id)
    end = page_num
    person = Person.query.offset((page_id-1)*page_num).limit(page_num)
    num1 = Person.query.count()
    num = math.ceil(num1/page_num)
    page_list = [i+1 for i in range(num)]
    page_prev = page_id - 1
    page_next = page_id + 1


    return render_template('index.html',
                           num=num, persons=person,
                           page_list=page_list, page_id=page_id,
                           page_next=page_next, page_prev=page_prev)





@blue.route('/sortp/<id>/')
def sortp(id):
    page_num = 3
    page = int(id)
    p = Person.query.paginate(page, page_num, False)
    persons = p.items
    print(p.items)#[<Person 10>]
    print(p.has_next)#False
    print(p.has_prev)#True
    print(p.page)#4
    print(p.pages)#4
    print(p.per_page)#3
    print(p.total)#10
    page_list = [i+1 for i in range(p.pages)]
    return render_template('paginator.html', persons=persons, p=p, page_list=page_list)


# @blue.route('/pageperson/<int:page>/')
@blue.route('/pageperson/')
def page_person():
    #  第几页      数据范围
    #    1        0-4
    #    2        5-9
    #    3        10-14
    #   ...
    #    page     (page-1)*page_num ~ page*page_num-1
    page = int(request.args.get('page'))
    page_num = 6  # 每页数据条数

    # 手动分页
    persons = Person.query.offset((page-1)*page_num).limit(page_num)

    # paginate
    p = Person.query.paginate(page, page_num, False)
    persons = p.items

    # print(p.items)
    # print(p.has_next)
    # print(p.has_prev)
    # print(p.page)
    # print(p.pages)
    # print(p.per_page)
    # print(p.total)

    return render_template('person_list.html', persons=persons, p=p)

