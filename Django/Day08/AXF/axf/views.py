from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

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
        'shop1':shop1,
        'shop2':shop[1:3],
        'shop3':shop[3:7],
        'shop4':shop[7:11],
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
    arr1 =childnames.split('#')
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
    return render(request, 'axf/cart.html')



def mine(request):
    return render(request, 'axf/mine.html')

from .forms.login import LoginForm


def login(request):
    print(request.method)
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            print(22)
            name = f.cleaned_data['username']
            pswd = f.cleaned_data['passwd']
            return HttpResponse(pswd)
        else:
            data = {
                'form': f,
                'error': f.errors
            }
            print(f.errors)
            return render(request, 'axf/login.html',data)
    else:
        f = LoginForm()
        return render(request, 'axf/login.html', {'form': f})



def register(request):
    return render(request, 'axf/register.html')

