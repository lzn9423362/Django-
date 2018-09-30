from django.shortcuts import render, redirect,reverse
from .models import Student
import datetime
# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request,'index.html',{'students':students})

def detail(request, stuid):
    stu = Student.objects.get(id=stuid) #获取student表中的id为1的对象
    return render(request, 'detail.html', {'stu':stu})

def detail2(request, id1, id2):
    print(id1,id2)
    stu = Student.objects.get(id=id2)
    return render(request,'detail.html',{'stu': stu})

def detail3(request, id1, id2):
    print(id1, id2)
    stu = Student.objects.get(id=id1)
    return render(request,'detail.html',{'stu':stu})


def success(request):

    # return render
    #重定向
    # return redirect('http://www.baidu.com')
    # return redirect(reverse('student:index')) #反向解析
    # return redirect(reverse('student:detail',args=[1])) #反向解析
    # return redirect(reverse('student:detail2', args=(1,2))) #反向解析,参数位置
    # return redirect(reverse('student:detail3', kwargs={'id1':2,'id2':3})) #反向解析


    name = '宝强'
    age = 20
    sex = True
    height = 1.65
    likes = ['马蓉', '林志玲', '李小璐', 'pgone', '白百何']
    citys = [
        ['深圳', '北京', '上海'],
        ['南极', '北级', '冬季'],
        ['格林尼治', '伦敦', '英国'],
        ['美国', '纽约', '华盛顿'],
    ]

    code2 = "<h1>hello</h1>"
    code3 ='<b>hello <script>  alert("猪头")  </script> </b>'

    data = {
        'name': name,
        'age': age,
        'sex': sex,
        'height':height,
        'likes':likes,
        'citys':citys,
        'now':datetime.datetime.now(),
        'code2':code2,
        'code3': code3,
    }

    return render(request, 'success.html', data)

