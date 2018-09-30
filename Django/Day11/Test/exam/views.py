import hashlib
import uuid
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from .models import User

def index1(request):
    username = request.session.get('name', '游客')
    return render(request, 'index1.html',{'username':username})

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        passwd = request.POST.get('passwd')
        f = request.FILES['img']
        print(f)
        file_name = generate_icon() + os.path.splitext(f.name)[-1]
        filePath = os.path.join(settings.MEDIA_ROOT, file_name)
        with open(filePath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)
                fp.flush()
        User.objects.create(user=user,passwd=passwd,img=file_name)
        return redirect(reverse('EXAM:index'))
    else:
        return render(request, 'index.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        users = User.objects.filter(user=username,passwd=passwd)
        if users.exists():
            user = users.first()
            request.session['name'] = username
            return HttpResponse('注册成功')
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return render(request, 'index1.html')

def generate_icon():

    #取随机id
    uid = str(uuid.uuid4())
    m = hashlib.md5()
    m.update(uid.encode())
    return m.hexdigest()