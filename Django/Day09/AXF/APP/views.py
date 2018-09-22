from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):

    #获取首页数据
    #轮播数据u
    wheels = MainWheel.objects.all()
    data = {
        'wheels': wheels,
    }
    return render(request, 'home/home.html', context=data)

def cart(request):
    return render(request, 'cart/cart.html')

def market(request):
    return render(request, 'market/market.html')

def mine(request):
    return render(request, 'mine/mine.html')