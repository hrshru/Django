from django.contrib import admin
from pig.models import Details

# Register your models here.
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Password', 'Email', 'ContactNo', 'DOB', 'Address']
admin.site.register(Details,DetailsAdmin)