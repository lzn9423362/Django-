from django.db import models

# Create your models here.

#用户和组:多对多
#组: 可以属于多个分组


#Group

class Group(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    password = models.CharField(max_length=200)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.name