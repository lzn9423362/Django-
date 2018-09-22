from django.conf.urls import url

from APP.views import *

urlpatterns =[
    url(r'^home/$', home, name='home'),
    url(r'^cart/$', cart, name='cart'),
    url(r'^market/$', market, name='market'),
    url(r'^mine/$', mine, name='mine'),
]