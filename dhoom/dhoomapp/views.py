from django.shortcuts import render, redirect
from django.http import HttpResponse
from dhoomapp.forms import StudentForm
from dhoomapp.models import Student


# Create your views here.
def student_image_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Gallary')
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})




def Gallary(request):
    if request.method == 'GET':
        Students = Student.objects.all()
        return render(request, 'display_image.html', {'student_images': Students})
