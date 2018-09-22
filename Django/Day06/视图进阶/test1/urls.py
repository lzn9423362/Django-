from django.conf.urls import url
from .views import *
urlpatterns = [
    # url(r'^', current_datetime),
    url(r'^index/', index),
    url(r'^att/', attribles),
    url(r'^get1/', get1),
    url(r'^get2/', get2),
    url(r'^showregist/regist/', regist),
    url(r'^showregist/', showregist),
    url(r'^showresponse/', showresponse),
    url(r'^cookietest/', cookietest),
    url(r'^redirect1/', redirect1),
    url(r'^redirect2/', redirect2),
    url(r'^main/', main),
    url(r'^login/', login),
    url(r'^showmain/', showmain),
    url(r'^quit/', quit),
    url(r'^display_meta/', display_meta),
]