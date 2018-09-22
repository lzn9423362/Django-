from django.conf.urls import url

from showtime.views import *

urlpatterns = [
    url(r'^show/', freshen),
    url(r'^index/', index1),
]