from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm

# Create your views here.
def UserFormView(request):
    return render(request,'file/registration.html')
