from django.conf.urls import url

from book.views import *

urlpatterns = [
    url(r'^index/', index,name='index'),
    url(r'^list/', list, name='list'),
    url(r'^detail/(\d+)/', detail, name='detail'),
]