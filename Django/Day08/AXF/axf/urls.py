from django.conf.urls import url

from .views import *
urlpatterns = [
    url(r'^home/', home, name='home'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', market, name='market'),
    url(r'^cart/', cart, name='cart'),
    url(r'^mine/', mine, name='mine'),
    url(r'^login/', login, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^checkuserid/', checkuserid, name='checkuserid'),
    url(r'^logout/', logout, name='logout'),
    url(r'^cartadd/', cartadd, name='cartadd'),
]
