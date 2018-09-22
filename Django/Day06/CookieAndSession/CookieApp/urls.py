from django.conf.urls import url

from CookieApp.views import *

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^login/', login, name='login' ),
    url(r'^loginhandle/', login_handle, name='loginhandle'),
    url(r'^logout/', logout, name='logout'),
    url(r'^showregist/', showregist, name='showregist'),
    url(r'^regist/', regist, name='regist'),
]