from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login as auth_login,logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.country = form.cleaned_data.get('country')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def login(request):
    if request.method == "POST":
        d = request.POST
        print(d)
        username = d['username']
        print(username)
        password = d['password']
        print(password)

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            print('success')
            return render(request,'dashboard.html')
        else:
            print('wrong')
            return redirect('social:login')
    return render(request,'registration/login.html')

# @login_required()
def dashboard(request):
    user=request.user
    return render(request,'dashboard.html',{'user':user})

# @login_required()
def profile(request):
    user = request.user
    return render(request,'profile.html',{'user':user})