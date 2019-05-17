from django import forms
from pig.models import Details
class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'