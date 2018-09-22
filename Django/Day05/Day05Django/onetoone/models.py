from django.db import models

# Create your models here.
class IdCard(models.Model):
    idnum = models.CharField(max_length=30)

    def __str__(self):
        return self.idnum

class Person(models.Model):
    name = models.CharField(max_length=20,default='老王')
    idcard = models.OneToOneField(IdCard)
    def __str__(self):
        return self.name