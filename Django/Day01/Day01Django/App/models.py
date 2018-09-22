from django.db import models

# Create your models here.

#创建模型
# MVT
# M: models.py
# v views.py
# T templates


#模型
class Grade(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField()
    girl_num = models.PositiveIntegerField() #正整数
    boy_num = models.IntegerField()
    is_delete = models.BooleanField(default=False)

class Student(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    age = models.IntegerField()
    info = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)
#类 = 表结构
#属性 = 表字段
#对象 = 表的一条记录

#models只要修改了，则需要通过数据迁移来让表同步

#数据迁移：
#生成迁移文件：Python manage.py makemigrations
#执行迁移文件: python manage.py migrate


