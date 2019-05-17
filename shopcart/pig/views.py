from django.shortcuts import render, redirect
from pig.models import Details
from pig.form import DetailsForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def retrieve_view(request):
    details = Details.objects.all()
    return render(request,'home.html', {'details': details})


def create_view(request):
    form = DetailsForm()
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Password = request.POST.get('Password')
        user = authenticate(Name=Name, Password=Password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(Name, Password))
            return HttpResponse("Invalid login details given so please go back and login properly")
    else:
        return render(request,'loging.html')









