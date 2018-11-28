from App.exts import db


# 下面写模型
# 城市字母分类
class CityLetter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    letter = db.Column(db.String(2))
    citys = db.relationship('City', backref='city_letter', lazy='dynamic')


# 城市
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parentId = db.Column(db.Integer, default=0)
    regionName = db.Column(db.String(100))
    cityCode = db.Column(db.Integer, unique=True)
    pinYin = db.Column(db.String(50))
    letter_id = db.Column(db.Integer, db.ForeignKey(CityLetter.id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True)
    is_active = db.Column(db.Boolean, default=False) #激活状态
    is_delete = db.Column(db.Boolean, default=False) #逻辑删除
    user_token = db.Column(db.String(100), unique=True)#usertoken
    permission = db.Column(db.Integer, default=11)



class Banner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(200))
    url = db.Column(db.String(200))


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    showname = db.Column(db.String(50))
    shownameen = db.Column(db.String(150))
    director = db.Column(db.String(50))
    leadingRole = db.Column(db.String(200))
    type = db.Column(db.String(100))
    country = db.Column(db.String(50))
    language = db.Column(db.String(50))
    duration = db.Column(db.String(50))
    screeningmodel = db.Column(db.String(50))
    openday = db.Column(db.DateTime)
    backgroundpicture = db.Column(db.String(150))
    flag = db.Column(db.Integer, default=1)
    isdelete = db.Column(db.Boolean,default=False)

class Cinemas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    score = db.Column(db.Float)
    hallnum = db.Column(db.Integer)
    servicecharge = db.Column(db.Integer)
    astrict = db.Column(db.Integer)
    flag = db.Column(db.Integer, default=1)
    isdelete = db.Column(db.Boolean, default=False)


