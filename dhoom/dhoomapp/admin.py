from django.contrib import admin
from dhoomapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['Name','Profile_Pics','Upload_video']


admin.site.register(Student,StudentAdmin)
