from django.http import HttpResponse
from django.shortcuts import render, redirect
from gallary import forms


# Create your views here.
def hotel_image_view(request):
    if request.method == 'POST':
        forms = HotelForm(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('success')
    else:
        forms = HotelForm()
    return render(request, 'index.html', {'forms': forms})


def success(request):
    return HttpResponse('successfuly uploaded')


def display_hotel_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
        return render((request, 'display_hotel_images.html',
                       {'hotel_images': Hotels}))
