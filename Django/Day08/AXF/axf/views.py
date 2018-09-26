import datetime
import hashlib
import random
import time
import uuid
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.cache import cache_page

from AXF import settings
from axf.models import *
from django.core.cache import cache


def home(request):
    print('我是home')
    wheel = MainWheel.objects.all()
    nav = MainNav.objects.all()
    mustbuy = MainMustbuy.objects.all()
    shop = MainShop.objects.all()
    shop1 = MainShop.objects.get(id=1)

    mainlist = MainShow.objects.all()
    data = {
        'wheels': wheel,
        'navs': nav,
        'mustbuys': mustbuy,
        'shop1': shop1,
        'shop2': shop[1:3],
        'shop3': shop[3:7],
        'shop4': shop[7:11],
        'main_list': mainlist,
    }
    return render(request, 'axf/home.html', data)


def market(request, categoryid, cid, sortid):
    leftSlider = MainFoodTpye.objects.all()
    if cid == '0':
        productList = Goods.objects.filter(categoryid=categoryid)
    else:

        productList = Goods.objects.filter(categoryid=categoryid, childcid=cid)
    if sortid == '1':
        productList = productList.order_by('-productnum')
    elif sortid == '2':
        productList = productList.order_by('-price')
    elif sortid == '3':
        productList = productList.order_by('price')

    group = leftSlider.get(typeid=categoryid)
    childList = []
    childnames = group.childtypenames
    arr1 = childnames.split('#')
    for str in arr1:
        arr2 = str.split(':')
        obj = {'childName': arr2[0], 'childId': arr2[1]}
        childList.append(obj)

    data = {
        'leftSlider': leftSlider,
        'productList': productList,
        'childList': childList,
        'categoryid': categoryid,
        'cid': cid,

    }
    return render(request, 'axf/market.html', data)


def cart(request):
    token = request.COOKIES.get('token', '')
    user = User.objects.filter(userToken=token)
    if user.exists():
        user = user.first()
        return render(request, 'axf/cart.html', {'user': user})
    else:
        return HttpResponseRedirect(reverse('AXF:login'))


def mine(request):
    token = request.COOKIES.get('token', '')
    user = User.objects.filter(userToken=token)
    if user.exists():
        user = user.first()

    return render(request, 'axf/mine.html', {'user': user})


from .forms.login import LoginForm


def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['username']
            pswd = f.cleaned_data['passwd']
            user = User.objects.filter(userAccount=name, userPasswd=my_md5(pswd))
            if user.exists():
                res = HttpResponseRedirect(reverse('AXF:mine'))
                d = datetime.datetime(3000, 1, 2, 3, 4, 5)  # 3000年后失效
                res.set_cookie('token', user.first().userToken, expires=d)
                return res
        else:
            data = {
                'form': f,
                'error': f.errors
            }
            return render(request, 'axf/login.html', data)
    else:
        f = LoginForm()
        return render(request, 'axf/login.html', {'form': f})


def logout(request):
    res = HttpResponseRedirect(reverse('AXF:mine'))
    res.delete_cookie('token')
    return res


def register(request):
    if request.method == 'POST':
        username = request.POST.get('userAccount')
        passwd = request.POST.get('userPasswd')
        email = request.POST.get('userAdderss')
        f = request.FILES['userImg']
        file_name = generate_icon() + os.path.splitext(f.name)[-1]
        filePath = os.path.join(settings.MDEIA_ROOT, file_name)
        with open(filePath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)
                fp.flush()
        User.objects.create(userAccount=username, userPasswd=my_md5(passwd), userAdderss=email, userImg=file_name,
                            userToken=generate_token())
        return HttpResponseRedirect(reverse('AXF:mine'))
    else:
        return render(request, 'axf/register.html')


from django.http import JsonResponse


# ajax请求,用户名认证
def checkuserid(request):
    userid = request.POST.get('userid')
    try:
        user = User.objects.get(userAccount=userid)
        return JsonResponse({'statu': 'error'})
    except User.DoesNotExist as e:
        return JsonResponse({'statu': 'success'})


def cartadd(request):
    token = request.COOKIES.get('token', '')
    # print(token)
    num = request.POST.get('num')
    goodid = request.POST.get('goodid')
    try:
        user = User.objects.get(userToken=token)
        good = Goods.objects.get(id=goodid)
        return JsonResponse({'status': 1, 'msg': 'ok'})
    except User.DoesNotExist as e:
        return JsonResponse({'status': 0, 'msg': 'error'})


# md5加密
# 生成32位16进制
# 不可逆
# 明文(字符串)和密文一对一
def my_md5(string):
    m = hashlib.md5()
    m.update(string.encode())
    return m.hexdigest()


# 生成加密的token
def generate_token():
    token = str(time.time()) + str(random.random())
    return my_md5(token)

    # 生成的唯一的图片名称


def generate_icon():
    # 取随机id
    uid = str(uuid.uuid4())
    m = hashlib.md5()
    m.update(uid.encode())
    return m.hexdigest()
