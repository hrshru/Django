from django import forms
from djapp4.models import Registration
class RegiForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'