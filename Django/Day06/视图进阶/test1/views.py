from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
from django.template import Template, Context


def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def index(request):
    return render(request, 'index.html')


def attribles(request):

    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)


    return HttpResponse('attribless')


# GET
# 访问方式http://127.0.0.1:8001/get1/?a=1&b=2&c=3
def get1(request):
    a = request.GET.get('a')  # get()方式
    b = request.GET['b']  # 字典方式
    c = request.GET.get('c')
    return HttpResponse(a + ' ' + b + ' ' + c)


# 访问方式http://127.0.0.1:8001/get2/?a=1&a=2&c=3
def get2(request):
    a = request.GET.getlist('a')  # 一个键对应多个值
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + ' ' + a2 + ' ' + c)


# POST
def regist(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    print(name, gender, age, hobby)

    return HttpResponse(name, gender)


def showregist(request):
    return render(request, 'regist.html')


def showresponse(request):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)  #
    print(res.charset)  # utf-8
    print(res.status_code)
    res.write()#追加
    # print(res.content-type)
    return res


# cookie

def cookietest(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write('<h1>' + cookie['sunck'] + '</h1>')
    # cookie = res.set_cookie('sunck', 'good')
    # 先存cookie,再执行上面的操作
    return res


# 重定向
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def redirect2(request):
    return HttpResponse('我是重定向后的视图')


def redirect1(request):
    # return HttpResponseRedirect('/redirect2')#重定向
    return redirect('/redirect2')  # 重定向推荐使用方法


# session
def main(request):
    # 取session

    username = request.session.get('name')
    if not username:
        username = '游客'
    return render(request, 'main.html', {'username':username})


def login(request):
    return render(request, 'login.html')


def showmain(request):

    username = request.POST.get('username')
    # 存储session
    request.session['name'] = username
    # request.session.set_expiry(5)#5秒后过期(整数)
    return redirect('/main')
#退出登录 清除session
from django.contrib.auth import logout
def quit(request):
    # logout(request)#第一种方式
    # request.session.clear()#第二种方式
    request.session.flush()#第三种方式
    # del request.session['name']
    #这种方式以游客方式清除会报服务器错误
    #session存值时期大概半个月

    # return redirect('/main')
    return redirect('/main')
#设置过期时间set_expiry(value),如果不设置,两个星期后过期
#整数set_expiry(value)
#时间对象
# 0关闭浏览器时失效
#None永不过期




def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
