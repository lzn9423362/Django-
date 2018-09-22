from django.conf.urls import url

from Student.views import *

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^detail/(\d+)$', detail, name='detail'),
    url(r'detail2/(\d+)/(\d+)/$', detail2, name='detail2'),
    url(r'detail3/(?P<id1>\d+)/(?P<id2>\d+)/$', detail3, name='detail3'),
    url(r'^success/', success, name='success')
]
