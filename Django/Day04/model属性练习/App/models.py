from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,verbose_name='姓名')
    # age = models.IntegerField(default=18)
    # address = models.TextField(default='深圳')
    # height = models.FloatField(default=1.80)
    # sex = models.BooleanField(default=True)
    # weight = models.DecimalField(max_digits=6, decimal_places=2,default=140.23)
    # n = models.NullBooleanField(default=True)
    # birthday = models.DateTimeField(auto_now=True) #自动更新最新一次修改的时间
    # birthday2 = models.DateTimeField(auto_now_add=True)#表创建时自动添加的时间，以后不会改变
    #
    # d = models.DateField(auto_now=True)
    # # t = models.DateTimeField()
    # img = models.ImageField()
    file = models.FileField()


    #http状态码
    #2xx 成功
    #3xx 重定向
    #4xx 客户端错误
    #5xx 服务断错误
    type_list = ((1,'青铜'),
                 (2,'白银用户'),
                 (3,'黄金用户'),
                 (4,'铂金用户'),
    )
    user_type = models.IntegerField(choices=type_list,default=1,verbose_name='段位')

    def __str__(self):
        return self.name