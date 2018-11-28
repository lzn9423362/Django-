from App.exts import db

# 下面写模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    passwd = db.Column(db.String(32))



class Banner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(200))


# "gid": 1002,
# "name": "Rolex",
# "price": 9699,
# "unit": "￥",
# "headImg": "/static/img/images/2.jpg"
class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gid = db.Column(db.Integer)
    name = db.Column(db.String(30))
    price = db.Column(db.Integer)
    unit = db.Column(db.String(150))
    headImg = db.Column(db.String(200))
