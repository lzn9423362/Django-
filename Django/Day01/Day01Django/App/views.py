from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


# MVT中的V

#  视图函数

def hello(request):
    return HttpResponse('hello world')

def abc(request):
    return HttpResponse('我爱你中华')

def index(request):

    #render:渲染
    name_list = ['强东', '马云', '马化腾', '马斯克']
    grade_list = Grade.objects.all() #获取Grade表的所有数据
    student_list = Student.objects.all()

    return render(request, 'index.html', {'names': name_list,'grades':grade_list,'students':student_list})

