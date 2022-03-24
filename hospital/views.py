from django.shortcuts import render


def home(request):
    return render(request,'hospital/home.html')
# Create your views here.

def bedManagement(request):
    return render(request,'hospital/bedavail.html')

def donation(request):
    return render(request,'hospital/donate.html')
