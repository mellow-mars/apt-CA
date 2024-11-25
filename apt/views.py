from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def information(request):
    return render(request, 'apt/information.html')

def location(request):
    return render(request, 'apt/location.html')

def direction(request):
    return render(request, 'apt/direction.html')