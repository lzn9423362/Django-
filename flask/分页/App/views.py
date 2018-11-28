import random

from flask import Blueprint, render_template, request
from sqlalchemy import and_, or_, not_, desc

from App.models import *


# 创建蓝图对象
blue = Blueprint('blue', __name__)
# 初始化蓝图
def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def home():
    return "home"


# 创建数据库和表
# @blue.route('/createdb/')
# def create_db():
#     db.create_all()
#     return "创建成功！"
#
#
# # 删除数据库表
# @blue.route('/dropdb/')
# def drop_db():
#     db.drop_all()
#     return "删除成功!"


# 增
# 添加一条数据
@blue.route('/addperson/')
def add_person():

    p = Person()
    p.name = "范冰冰" + str(random.randint(10,99))
    p.age = random.randint(10, 99)

    try:
        # 执行添加操作
        db.session.add(p)
        db.session.commit()
    except:
        # 回滚
        db.session.rollback()
        db.session.flush()

    return "添加Person成功!"


# 同时添加多条数据
@blue.route('/addpersons/')
def add_persons():

    persons = []
    for i in range(100,110):
        p = Person()
        p.name = "李晨" + str(i)
        p.age = i - 60
        persons.append(p)

    # 执行添加操作
    db.session.add_all(persons)
    db.session.commit()

    return "添加多个Person成功！"


# 删
@blue.route('/delperson/')
def del_person():
    # 获取主键为2的对象
    p = Person.query.get(2)

    # 执行删除操作
    db.session.delete(p)
    db.session.commit()

    return "删除成功!"


# 改
@blue.route('/modifyperson/')
def modify_person():
    # 获取主键为1的对象
    p = Person.query.get(1)
    # print(p)  # <Person 1>
    # print(type(p))  # <class 'App.models.Person'>
    # print(Person.query)
    # print(type(Person.query))  # <class 'flask_sqlalchemy.BaseQuery'>
    # print(list(Person.query))  # [<Person 1>, <Person 3>, <Person 4>, <Person 5>, <Person 6>, <Person 7>, <Person 9>, <Person 10>, <Person 11>, <Person 13>, <Person 14>, <Person 15>, <Person 16>, <Person 17>, <Person 18>, <Person 19>, <Person 20>, <Person 21>, <Person 22>, <Person 23>]

    p.age = 16
    db.session.commit()

    return "修改成功!"


# 查询
@blue.route('/getperson/')
def get_person():
    # 查询所有数据
    # persons = Person.query.all()
    # print(persons)  # [<Person 1>, <Person 6>,...]
    # print(type(persons))  # <class 'list'>

    # persons = Person.query.filter(Person.age<=42)
    # persons = Person.query.filter_by(age=42)  # 一般做等值条件过滤

    persons = Person.query.filter(Person.age.__gt__(42))  # >
    persons = Person.query.filter(Person.age.__ge__(42))  # >=
    persons = Person.query.filter(Person.age.__lt__(42))  # <
    persons = Person.query.filter(Person.age.__le__(42))  # <=

    persons = Person.query.filter(Person.name.startswith('范'))
    persons = Person.query.filter(Person.name.endswith('8'))
    persons = Person.query.filter(Person.name.contains('1'))
    persons = Person.query.filter(Person.age.in_([10, 20, 30, 40, 50]))

    persons = Person.query.filter(Person.age>=20, Person.age<=40)
    persons = Person.query.filter(and_(Person.age>=20, Person.age<=40))
    persons = Person.query.filter(or_(Person.age>=20, Person.age<=40))
    persons = Person.query.filter(not_(and_(Person.age>=20, Person.age<=45)))

    # print(persons)
    # print(type(persons))  # <class 'flask_sqlalchemy.BaseQuery'> 
    return render_template('person_list.html', persons=persons)


# 排序
@blue.route('/sortperson/')
def sort_person():

    persons = Person.query.limit(5)  # 限制获取前5个
    persons = Person.query.offset(5)  # 跳过前5个
    persons = Person.query.order_by('age')  # 按年龄升序
    persons = Person.query.order_by('-age')  # 按年龄降序
    # persons = Person.query.order_by(desc('age'))  # 按年龄降序

    return render_template('person_list.html', persons=persons)


# 分页
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
    # persons = Person.query.offset((page-1)*page_num).limit(page_num)

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











