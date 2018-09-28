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
    url(r'^cartaddto/', cartaddto, name='cartaddto'),
    url(r'^cartadd/', cartadd, name='cartadd'),
    url(r'^cartnumadd/', cartnumadd, name='cartnumadd'),
    url(r'^cartnumreduce/', cartnumreduce, name='cartnumreduce'),
    url(r'^cartdel/', cartdel, name='cartdel'),
    url(r'^cartselect/', cartselect, name='cartselect'),
    url(r'^cartallselect/', cartallselect, name='cartallselect'),
    url(r'^orderadd/', orderadd, name='orderadd'),
    url(r'^order/(\d+)/', order, name='order'),
    url(r'^pay/', pay, name='pay'),
    url(r'^orderunpay/', orderunpay, name='orderunpay'),
    url(r'^ordernopayhandle/', ordernopayhandle, name='ordernopayhandle'),
    url(r'^orderunreceive/', orderunreceive, name='orderunreceive'),
    url(r'^orderconfirm/', orderconfirm, name='orderconfirm'),
]
