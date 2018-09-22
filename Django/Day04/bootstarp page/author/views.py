from django.shortcuts import render
from .models import *
# Create your views here.
import math
def index(request):
    authors = Author.objects.all()
    return render(request, 'author/index.html', {'authors':authors})



def detail(request,author_id):
    author = Author.objects.get(id=author_id)
    return render(request,'author/detail.html',{'author':author})


def page1(request):
    return page(request, 1)

#分页
def page(request,page):
    per_num = 3 #每页数量
    start = (int(page) - 1) * per_num
    end = start + per_num
    authors = Author.objects.all()
    #总页数
    pages = math.ceil(authors.count() / per_num)
    page_list = [i+1 for i in range(pages)]
    page_next = int(page) + 1 #上一页

    page_prev = int(page) - 1  #
    if page_prev == 0:
        page_prev = 1
    if page_next == pages + 1:
        page_next = pages
    page2 = int(page)
    if page2 == pages+1:
        page2 = 1



    return render(request,'author/page.html',{'authors':authors[start:end], 'pages_list':page_list, 'page_prev':page_prev, 'page_next':page_next,'page2':page2})