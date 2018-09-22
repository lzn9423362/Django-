from django.conf.urls import url

from ViewApp.views import *

urlpatterns = [
    url(r'^index/', index),
]