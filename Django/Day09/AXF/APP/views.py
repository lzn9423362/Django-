from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):

    #获取首页数据
    #轮播数据u
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
    return render(request, 'home/home.html', data)
def cart(request):
    return render(request, 'cart/cart.html')

def market(request):
    return render(request, 'market/market.html')

def mine(request):
    return render(request, 'mine/mine.html')