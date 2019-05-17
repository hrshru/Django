from django import forms
from dhoomapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['Name','Profile_Pics','Upload_video']
