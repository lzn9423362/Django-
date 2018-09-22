from django.conf.urls import url

from newday.views import *

urlpatterns = [
    url(r'^index/', index),
    url(r"^upfile/", upfile),
    url(r"^savefile/", savefile),
    url(r"^ajaxstudents/", ajaxstudents),
    url(r'^studentsinfo/', studentsinfo),
    url(r'^edit/', edit),
    url(r'^userlist/', user_list, name='userlist'),
    url(r'^userdetail/(\d+)/', user_detail, name='userdetail'),
]