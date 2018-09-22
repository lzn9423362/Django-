from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^index2/', index2, name='index2'),
]
