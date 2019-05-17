from django.contrib import admin
from djapp3.models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_Id', 'product_name', 'desc', 'prize', 'pub_date', 'image']
admin.site.register(Product,ProductAdmin)