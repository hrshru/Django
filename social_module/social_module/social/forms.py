from django import forms
from .models import Profile,User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper

class SignUpForm(UserCreationForm):
    Choice= ((None,'Select gender'),('M','Male'), ('F','Female'),('O','Other'), )
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    birth_date = forms.DateField()
    gender = forms.ChoiceField(choices=Choice)
    country = forms.CharField(max_length='100')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','gender','country' )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image','country', 'city','state','fullAddress')