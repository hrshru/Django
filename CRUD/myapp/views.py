from django.shortcuts import render,redirect
from myapp.models import Employee
from myapp.form import EmployeeForm

# Create your views here.
def retrive_view(request):
    employee = Employee.objects.all()
    return render(request, 'index.html', {'employee':Employee})
def create_view(request):
    form = EmployeeForm()
    if request.method =='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/index')
    return render(request,'create.html',{'form':form})
def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/index')
def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method =='POST':
        form =EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/index')
        return render(request,'update.html',{'employee':Employee})