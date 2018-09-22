from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from myapp.models import User


def index(request, num):
    users = User.objects.all()
    p = Paginator(users, 5)  # 创建分页对象
    # print(p.num_pages) #总页数,3
    # print(p.count) #数据总数, 14
    # print(p.page_range) #页码范围range(1,4)
    # print(p.per_page) #每页数据数量, 5

    # 创建page对象
    page = p.page(num)
    # print(page.number)#当前页码
    # print(page.object_list)#当前页码的数据

    # #page对象的方法
    # print(page.has_next())
    # print(page.has_previous())
    # print(page.has_other_pages())
    # print(page.next_page_number())
    # print(page.previous_page_number()) #上一页的页码,不存在会报错

    data = {
        'page': page,
        'page_range': p.page_range,
    }

    return render(request, 'myapp/index.html', data)
