from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Profile_Pics=models.ImageField(upload_to='photos/')
    Upload_video= models.FileField(upload_to='videos/',)
    def __str__(self):
        return self.Name
