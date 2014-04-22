# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

# Create your models here.
