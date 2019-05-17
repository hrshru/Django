from django.contrib import admin
from cart.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductName','Details','Prize','Product_pic']
admin.site.register(Product,ProductAdmin)