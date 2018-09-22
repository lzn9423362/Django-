import hashlib
import random
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import *
from django.utils.encoding import smart_str
# Create your views here.


#首页
def index(request):
    #user = request.COOKIES.get('user','')
    #user = request.session.get('user','')
    token = request.COOKIES.get('token', '')
    users = UserModel.objects.filter(token=token)
    user = ''
    if users.exists():
        user = users.first().user
    return render(request, 'CookieApp/index.html', {'user': user})

def login(request):
    return render(request, 'CookieApp/login.html')


import datetime
def login_handle(request):
   if request.method == 'GET':
    username = request.GET.get('username')
    password = request.GET.get('password')
    users = UserModel.objects.filter(user=username, passwd=my_md5(password))
    if users.exists():
        response = HttpResponse('登录成功')

        # response.set_cookie('user', username) #如果未设置,默认时回话结束时cookie失效
        # d = datetime.datetime.now() + datetime.timedelta(days=10) #十天后
        d = datetime.datetime(3000,1,2,3,4,5)#3000年后失效
        response.set_cookie('token', users.first().token,expires=d)

        def cookie_set(request):
            response = HttpResponse("<h1>设置Cookie，请查看响应报文头</h1>")

            return response
        return response
    else:
        return HttpResponse('用户名或者密码错误')
   else:
       return HttpResponse('请求方式错误!')


def logout(request):
    response = HttpResponseRedirect(reverse('CookieApp:index'))
    #cookie
    response.delete_cookie('token')
    return response


def regist(request):
    userregist = request.GET.get('registuser')
    passwdregist = request.GET.get('registpasswd')
    users = UserModel.objects.filter(user=userregist)
    if users.exists():
        return HttpResponse('该账号已存在')
    else:
        response = HttpResponse()
        UserModel.objects.create(user=userregist,passwd=my_md5(passwdregist), token=generate_token())
        # response.set_cookie('user', userregist)
        return HttpResponse('注册成功')

def showregist(request):
    return render(request, 'CookieApp/regist.html')


#md5加密
#生成32位16进制
#不可逆
#明文(字符串)和密文一对一
def my_md5(string):
    m = hashlib.md5()
    m.update(string.encode())
    return m.hexdigest()


# 生成加密的token
def generate_token():
    token = str(time.time()) + str(random.random())
    return my_md5(token)
