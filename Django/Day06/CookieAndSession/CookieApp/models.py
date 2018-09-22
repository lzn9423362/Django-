
from django.db import models

# Create your models here.


class UserModel(models.Model):
    user = models.CharField(max_length=20, unique=True)
    passwd = models.CharField(max_length=32)
    token = models.CharField(max_length=32, default='', null=True, blank=True)
