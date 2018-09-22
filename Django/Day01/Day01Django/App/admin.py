from django.contrib import admin
from .models import *
# Register your models here.


#后台管理：管理表


#在后台管理页面中注册模型Grade:后台可以管理Grade表
admin.site.register(Grade)

admin.site.register(Student)