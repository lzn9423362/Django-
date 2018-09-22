from django.db import models

# Create your models here.


class UserType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

def fn():
    return 3

class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    user_type =  models.ForeignKey(UserType, on_delete=models.CASCADE) #默认值,级联删除,删除UserTpye
    # user_type =  models.ForeignKey(UserType, on_delete=models.PROTECT) #保护,阻止删除
    # user_type =  models.ForeignKey(UserType, on_delete=models.SET_NULL,null=True) #删除时设置为null
    # user_type =  models.ForeignKey(UserType, on_delete=models.SET_DEFAULT,default=2) #删除时设置为default,之前为null的值也都成了默认值
    # user_type =  models.ForeignKey(UserType, on_delete=models.SET(fn)) #删除时设置为指定值
    # user_type =  models.ForeignKey(UserType, on_delete=models.DO_NOTHING()) #删除时不会影响其他表




    def __str__(self):
        return self.name