from django.shortcuts import render,redirect
from loginapp.models import *
from loginapp.forms import *
from django.contrib.auth.models import User

# Create your views here.
def retrieve_view(request):
    employee = Employee.objects.all()
    return render(request,'signup.html',{'employee':employee})
def create_view(request):
    form=EmployeeForm()
    if request.method =='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'create.html', {'form':form})
def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')
def update_view(request,id):
    employee=Employee.objects.get(id=id)
    return render(request, 'update.html', {'employee': employee})
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()

    return redirect('/')