from django.conf.urls import url

from .views import *
#子路由
# from App.views import hello

urlpatterns = [
    url(r'^hello/', hello),
    url(r'^abc/$', abc),
    url(r'index/', index),

]