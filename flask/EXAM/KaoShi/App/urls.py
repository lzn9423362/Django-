from App.apis.GoodsApi import GoodsResource
from App.apis.LoginApi import LoginResource
from App.apis.RegisterApi import RegisterResource
from App.exts import api
from App.apis.BannerApi import *


# 路由
api.add_resource(BannerResource, '/banner/')
api.add_resource(GoodsResource, '/goods/')
api.add_resource(RegisterResource, '/registers/')
api.add_resource(LoginResource, '/logins/')


