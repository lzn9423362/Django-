from django.shortcuts import render

# Create your views here.
from axf.models import *


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
        'shop1':shop1,
        'shop2':shop[1:3],
        'shop3':shop[3:7],
        'shop4':shop[7:11],
        'main_list': mainlist,
    }
    return render(request, 'axf/home.html', data)


def market(request):
    leftSlider = MainFoodTpye.objects.all()
    productList = Goods.objects.all()
    data = {
        'leftSlider': leftSlider,
        'productList':productList,
    }
    return render(request, 'axf/market.html', data)


def cart(request):
    return render(request, 'axf/cart.html')


def mine(request):
    return render(request, 'axf/mine.html')


