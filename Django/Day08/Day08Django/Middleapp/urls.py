from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^verify/', generater_verify, name='verify'),
    url(r'^login/', login, name='login'),


]
