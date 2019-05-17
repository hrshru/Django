from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"store/dj3html2.html")
def about(request):
    return HttpResponse("this is  About Us ")
def contact(request):
    return HttpResponse("this is  Contact Us ")
def tracker(request):
    return HttpResponse("this is  track Us ")
def search(request):
    return HttpResponse("this is  Search Us ")
def product(request):
    return HttpResponse("this is  productviews ")
def checkout(request):
    return HttpResponse("this is  Checkout ")