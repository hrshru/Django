from django.db import models

# Create your models here.
class Product(models.Model):
    ProductName = models.CharField(max_length=30)
    Details = models.CharField(max_length=150)
    Prize = models.FloatField()
    Product_pic = models.ImageField(upload_to="photos/image", default="")

    def __str__(self):
        return self.ProductName