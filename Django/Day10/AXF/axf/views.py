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
        cart = Cart.objects.filter(userAccount=user.userAccount)

        return render(request, 'axf/cart.html', {'user': user,'cart': cart})
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

# market中添加到购物车
def cartaddto(request):
    token = request.COOKIES.get('token', '')
    num = request.POST.get('num')
    goodid = request.POST.get('goodid')
    good = Goods.objects.get(id=goodid)  # 商品

    try:
        # 查询用户是否登录
        user = User.objects.get(userToken=token)  # 当前用户
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = None
        # 如果订单不存在就添加订单
        if not carts.exists():

            c = Cart(userAccount=user.userAccount, productid=goodid,
                     productnum=num, productprice=good.price,
                     isChose=True, productimg=good.productimg,
                     productname=good.productlongname, isDelete=False)
            c.save()
            good.storenums -= int(num)
            good.save()
        # 存在订单就加商品数量
        else:
            try:
                # 查询订单是否有该商品
                c = carts.get(productid=goodid)

                c.productnum += int(num)
                # onecart.productprice = '%.2f'%(float(good.price) * onecart.productnum)
                c.save()
                good.storenums -= int(num)
                good.save()
            except Cart.DoesNotExist as e:

                c = Cart(userAccount=user.userAccount, productid=goodid,
                         productnum=num, productprice=good.price,
                         isChose=True, productimg=good.productimg,
                         productname=good.productlongname, isDelete=False)
                c.save()
                good.storenums -= int(num)
                good.save()
        return JsonResponse({'status': 1, 'msg': 'ok'})
    except User.DoesNotExist as e:
        return JsonResponse({'status': 0, 'msg': 'error'})

#market中验证库存
def cartadd(request):
    num = request.POST.get('num')
    goodid = request.POST.get('goodid')
    try:
        good = Goods.objects.get(id=goodid)
        storenums = good.storenums
        if (storenums < int(num)):
            return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 2})
    except:
        return JsonResponse({'status': 0})


#增加购物车的商品数
def cartnumadd(request):
    cartid = request.POST.get('cartid')
    try:
        cart = Cart.objects.get(id=cartid)
        cart.productnum += 1
        cart.save()
        num = cart.productnum
        return JsonResponse({'status': 1, 'num': num})
    except:
        pass
#减少购物车的商品数量
def cartnumreduce(request):
    cartid = request.POST.get('cartid')
    token = request.COOKIES.get('token', '')
    try:
        cart = Cart.objects.get(id=cartid)
        user = User.objects.filter(userToken=token)
        if user.exists():
            if(cart.productnum>1):
                cart.productnum -= 1
                cart.save()
            num = cart.productnum
            return JsonResponse({'status': 1, 'num': num})
        else:
            return JsonResponse({'status': 0})
    except:
        return JsonResponse({'msg': 'error'})

# 将购物车的数据删除
def cartdel(request):
    cartid = request.POST.get('cartid')
    token = request.COOKIES.get('token', '')
    try:
        cart = Cart.objects.get(id=cartid)
        user = User.objects.filter(userToken=token)
        if user.exists():
            cart.delete()

            return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 0})
    except:
     return JsonResponse({'msg': '订单不存在'})

#ajax请求前端传来cart的id 将数据库中的选择状态数据取反,并传给前端
def cartselect(request):
    cartid = request.POST.get('cartid')
    token = request.COOKIES.get('token', '')
    try:
        cart = Cart.objects.get(id=cartid)
        user = User.objects.filter(userToken=token)
        if user.exists():
            cart.isChose = not cart.isChose
            cart.save()

            return JsonResponse({'status': 1, 'select': cart.isChose})
        else:
            return JsonResponse({'status': 0})
    except:
        return JsonResponse({'msg': '订单不存在'})

#全选ajax请求,
def cartallselect(request):
    if request.method == 'POST':
        token = request.COOKIES.get('token', '')
        try:
            user = User.objects.get(userToken=token)
            carts = Cart.objects.filter(userAccount=user.userAccount)
            flag = 0
            maxcart = carts.count()
            for cart in carts:        #如果购物车所有商品的选择状态都为 True 就将所有的isChose改为false 存入数据库中,否则则全改为true,状态码都为1
                if cart.isChose == True:
                    flag += 1
            if flag == maxcart:
                for cart in carts:
                    cart.isChose = False
                    cart.save()
                return JsonResponse({'status': 1})
            else:
                for cart in carts:
                    cart.isChose = True
                    cart.save()
                return JsonResponse({'status': 1})
        except User.DoesNotExist as e:
            return JsonResponse({'msg': '错是不可能错的'})

#添加订单
def orderadd(request):
    if request.method == 'POST':
        token = request.COOKIES.get('token', '')
        try:
            user = User.objects.get(userToken=token)
            carts = Cart.objects.filter(userAccount=user.userAccount, isChose=True) #状态为已经选择的商品查询出来,并加到订单当中
            if not carts.exists():
                return JsonResponse({'status': -1})
            else:
                oid = generate_icon()
                num = request.POST.get('num')
                o = Order.objects.create(orderid=oid, userid=user.userAccount, progress=0, money=num) #保存订单信息存金额,用户,订单号,和用户
                for cart in carts:
                    cart.isDelete = True #将已经加到订单里的购物车内商品状态逻辑删除(即数据还保存在数据库中)
                    cart.orderid = oid    #订单号存入逻辑删除的购物车商品中,到时候可以定义model的manager来查询
                    cart.save()
                orderid = o.id
                return JsonResponse({'status': 1, 'orderid': orderid})
        except:
            return JsonResponse({'status': 'error2'})
    return JsonResponse({'status': 'error'})

#渲染order将订单数据传到order.html
def order(request, id):
    order = Order.objects.get(id=id)
    carts = Cart.objects1.filter(orderid=order.orderid)
    sum = 0
    for cart in carts:
       sum += float(cart.productprice) * int(cart.productnum)
    data = {'carts': carts, 'sum': sum, 'orderid': order.orderid, 'id': id}
    return render(request, 'axf/order.html', data)

#支付,ajax请求将订单id传过来
def pay(request):
    if request.method == 'POST':
        token = request.COOKIES.get('token', '')
        id = request.POST.get('id')
        user = User.objects.filter(userToken=token)
        if user.exists():
            order = Order.objects.get(id=id) #查询相应订单
            order.progress = 1 #改变订单状态,改为支付状态
            order.save()
            return JsonResponse({'status': 1}) #如果为1,支付完则跳转到mine页面
        else:
            return JsonResponse({'msg': 'error'})
    else:
        return JsonResponse({'msg': 'error'})

# 将未支付订单渲染出来
def orderunpay(request):
    token = request.COOKIES.get('token', '')
    user = User.objects.filter(userToken=token)
    sum = 0
    orders = Order.objects.filter(userid=user.first().userAccount, progress=0)#查询支付process为0 即未支付的订单
    carts = Cart.objects1.all()#查询所有的购物车, 在前端进行判断
    return render(request, 'axf/orderunpay.html', {'orders': orders, 'carts': carts})

# 将未支付订单状态process改为1,并在前端将支付节点删除
def ordernopayhandle(request):
    if request.method == 'POST':
       orderid = request.POST.get('orderid')
       order = Order.objects.get(id=orderid)
       order.progress = 1
       order.save()
       return JsonResponse({'status': 1})



def orderunreceive(request):
    orders = Order.objects.filter(progress=1)
    carts = Cart.objects1.all()
    data = {
        'orders': orders,
        'carts': carts,
    }
    return render(request, 'axf/orderunreceive.html', data)


def orderconfirm(request):
    if request.method == 'POST':
        try:
            orderid = request.POST.get('orderid')
            print(orderid)
            order = Order.objects.get(id=orderid)
            print(12)
            order.progress = 2
            order.save()
            return JsonResponse({'status': 1})
        except:
            return JsonResponse({'status': 0, 'msg': 'error'})
    else:
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

