from django.db import models

# Create your models here.
class Product(models.Model):
    product_Id = models.AutoField(default=1)
    product_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    prize = models.IntegerField(default=0)
    pub_date = models.DateField
    image = models.ImageField(upload_to="shop/image", default="")