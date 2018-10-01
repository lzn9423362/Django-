from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^register/', register, name='register'),
    url(r'^registerhandle/', registerhandle, name='registerhandle'),
    url(r'^login/', login, name='login'),
    url(r'^loginhandle/', loginhandle, name='loginhandle'),
    url(r'^logout/', logout, name='logout'),
    url(r'^loginajax/', loginajax, name='loginajax'),
]
