import hashlib
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    return render(request, 'index.html')


def upfile(request):
    return render(request, 'upfile.html')


import os
from django.conf import settings


def savefile(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = USermodel.objects.filter(name=username)
        if not user.exists():
            f = request.FILES['file']
            # 文件在服务器端的路径

            #自己生成的唯一名称
            file_name = generate_icon() + os.path.splitext(f.name)[-1]
            filePath = os.path.join(settings.MDEIA_RROT, file_name)

            with open(filePath, 'wb') as fp:
                for info in f.chunks():
                    fp.write(info)
                    fp.flush()
            USermodel.objects.create(name=username, icon=file_name)
             # 2.将文件路径存入数据库
            return HttpResponse('上传成功')
        else:
            return HttpResponse('用户名已存在')
    else:
        return HttpResponse('上传失败')


#生成的唯一的图片名称
def generate_icon():

    #取随机id
    uid = str(uuid.uuid4())
    m = hashlib.md5()
    m.update(uid.encode())
    return m.hexdigest()


def user_list(request):
    users = USermodel.objects.all()
    print(users)
    return render(request, 'list.html', {'users': users})



def user_detail(request,userid):
    user = USermodel.objects.get(id=userid)
    return render(request, 'detail.html', {'user':user})





from django.core.paginator import Paginator


def studentpage(request, pageid):
    # allList = Student.objects.all()
    # paginator = Paginator(allList,6)
    # page = paginator.page(pageid)
    # 千峰视频高级使用6 分页
    # return render(request, '',{'student': page})
    pass


#ajax请求
def ajaxstudents(request):
    return render(request, 'ajaxstudents.html')

#请求的url视图函数
def studentsinfo(request):
    stus = Students.objects.all()
    list = []
    for stu in stus:
        list.append([stu.name, stu.age])
    return JsonResponse({'data': list})


def edit(request):
    return render(request, 'edit.html')
