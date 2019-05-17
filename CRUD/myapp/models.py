from django.db import models

# Create your models here.
class Employee(models.Model):
    Eno = models.IntegerField()
    Ename = models.CharField(max_length=64)
    Esal = models.FloatField()
    Eaddr = models.CharField(max_length=258)