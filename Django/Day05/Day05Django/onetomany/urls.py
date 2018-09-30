from django.conf.urls import url
from .views import *

urlpatterns = [
    url('index/', index, name='index')
]
