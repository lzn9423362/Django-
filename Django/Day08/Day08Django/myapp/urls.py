from django.conf.urls import url

from myapp.views import *

urlpatterns = [
    url(r'^index/(\d+)/', index, name='index')
]
