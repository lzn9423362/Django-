from django.db import models

# Create your models here.

class Main(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True #抽象类

#首页-轮播
class MainWheel(Main):
    class Meta:
        db_table = 'axf_wheel'


#首页-导航
class MainNav(Main):
    class Meta:
        db_table = 'axf_nav'


#首页-必须购买
class MainMustbuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'


#首页-购买
class MainShop(Main):
    class Meta:
        db_table = 'axf_shop'