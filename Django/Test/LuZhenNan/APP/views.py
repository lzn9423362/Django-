import hashlib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
# Create your views here.


def index(request):
    username = request.session.get('username')
    users = User.objects.filter(username=username)
    user = users.first()
    girl = Girl.objects.all()
    man = Man.objects.all()

    if users.exists():
        user = users.first()
        return render(request, 'index.html', {'user': user, 'girl1': girl[0:1], 'girl2':girl[1:6], 'man1': man[0:2], 'man2': man[2:11]
})
    else:
        return render(request, 'index.html', {'user':user, 'girl1': girl[0:1], 'girl2':girl[1:6], 'man1': man[0:2], 'man2': man[2:11]
})
# 'girl1': girl[0:2], 'girl2':girl[2:7], 'man1': Man[0:2], 'man2': Man[2:11]

def register(request):
    return render(request, 'register.html')


def registerhandle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create(username=username, password=password, email=email)
        return redirect(reverse('APP:login'))



def login(request):
    return render(request, 'login.html')


def loginhandle(request):
    if request.method == 'POST':
        username = request.POST.get('phone')
        password = request.POST.get('password')
        users = User.objects.filter(username=username, password=password)
        if users.exists():
            request.session['username'] = users.first().username

            return redirect(reverse('APP:index'))
        else:
            return HttpResponse('账号密码错误')
    else:
        return HttpResponse('请求方式错误')

def logout(request):
    request.session.clear()
    return redirect(reverse("APP:index"))


def loginajax(request):
    username = request.POST.get('value')
    try:
        user = User.objects.get(username=username)
        return JsonResponse({'status': 0})
    except:
        return JsonResponse({'status': 1})



def my_md5(string):
    m = hashlib.md5()
    m.update(string.encode())
    return m.hexdigest()
