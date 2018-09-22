from django.conf.urls import url

from author.views import *

urlpatterns = [
    url(r'^index/', index, name='index'),

    # url(r'^detail/', detail, name='detail'),
    url(r'^detail/(\d+)/', detail, name='detail'),
]