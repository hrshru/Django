from django.db import models

# Create your models here.
class Details(models.Model):
    Name = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Email = models.EmailField()
    ContactNo = models.IntegerField()
    DOB = models.DateField()
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name