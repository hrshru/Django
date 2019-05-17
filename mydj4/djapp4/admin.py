from django.contrib import admin
from djapp4.models import Registration
# Register your models here.
class RegAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Date_of_Birth', 'Profile_pic']
admin.site.register(Registration,RegAdmin)