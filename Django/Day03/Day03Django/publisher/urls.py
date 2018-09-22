from django.conf.urls import url

from publisher.views import *

urlpatterns = [
    url(r'^index/', index,name='index'),
    url(r'^detail/(\d+)/',  detail, name='detail'),
]