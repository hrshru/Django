from django.shortcuts import render,redirect
from testapp.models import Student
from testapp.forms import StudentForm

# Create your views here.
def retrieve_view(request):
    student=Student.objects.all()
    return render(request,'testapp/index.html',{'student':student})

def create_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/index')
    return render(request,'testapp/create.html',{'form':form})

def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/index')

def update_view(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'testapp/update.html',{'student':student})
    
