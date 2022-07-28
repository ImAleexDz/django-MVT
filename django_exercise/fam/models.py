from turtle import back
from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, null=True)
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField(default=0)


