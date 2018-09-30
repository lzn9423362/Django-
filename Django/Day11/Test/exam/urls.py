from django.conf.urls import url
from.views import *

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^index1/', index1, name='index1'),
    url(r'^register/', register, name='register'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
]
