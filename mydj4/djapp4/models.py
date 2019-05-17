from django.db import models

# Create your models here.
class Registration(models.Model):
    Name = models.CharField(max_length=30)
    Date_of_Birth = models.DateField()
    Profile_pic = models.ImageField(upload_to="photos/image", default="", blank=True)