import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.decorators.cache import cache_page

from CacheApp.models import User


@cache_page(10)
def index(request):
    print('进入了index视图函数')
    time.sleep(5)
    return render(request, 'CacheApp/index.html')


def index2(request):

    # 1.先获取缓存中的数据
    cache_data = cache.get('users')
    if cache_data:
        result = cache_data
    #2.如果没有缓存数据,则查询数据库
    else:
        users = User.objects.all()
        time.sleep(3)
        template = loader.get_template('CacheApp/index2.html')
        result = template.render({'users': users})
        print(result)
    # return render(request, 'CacheApp/index2.html', result)

        #2.设置缓存
        cache.set('users', result, 60)


    return HttpResponse(result)