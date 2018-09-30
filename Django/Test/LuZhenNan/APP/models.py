from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=50)


class Girl(models.Model):
    img = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

class Man(models.Model):
    img = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)