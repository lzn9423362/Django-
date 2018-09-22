from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20)


    def __str__(self):
        return self.name

from tinymce.models import HTMLField
class Text(models.Model):
    str = HTMLField()


class USermodel(models.Model):
    name = models.CharField(max_length=20,unique=True)
    icon = models.CharField(max_length=200)