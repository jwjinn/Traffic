from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def seoulIndex(request):
    return render(request, 'seoulIndex.html')

def roadTraffic(request):
    return render(request, 'roadTraffic.html')

def bus(request):
    return render(request, 'bus.html')

def subway(request):
    return render(request, 'subway.html')