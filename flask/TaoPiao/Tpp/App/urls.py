from App.apis.BannerApi import BannerResource
from App.apis.CinemasApi import CinemasResource
from App.apis.LoginApi import Login
from App.apis.MoviesApi import MoviesResource
from App.apis.PermissionApi import PermissionResource
from App.apis.UserActive import UserActiveResource
from App.apis.UserRegisterApi import Register
from App.exts import api
from App.apis.CityApi import *
# 路由
api.add_resource(CityResource, '/citys/')
api.add_resource(Register, '/register/')
api.add_resource(Login, '/login/')
api.add_resource(UserActiveResource, '/active/')
api.add_resource(PermissionResource, '/permission/')
api.add_resource(BannerResource, '/banner/')
api.add_resource(MoviesResource, '/movies/')
api.add_resource(CinemasResource, '/cinemas/')
