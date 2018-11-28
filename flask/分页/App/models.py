# 模型
from App.exts import db


# Person模型
class Person(db.Model):
    __tablename__ = 'Person'  # 表名
    # id字段：类型为整型，主键，自动增加
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # name字段: 类型为字符串，唯一
    name = db.Column(db.String(16), unique=True)
    # age字段: 类型是整型，默认值是1
    age = db.Column(db.Integer, default=1)


# Teacher模型
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)


