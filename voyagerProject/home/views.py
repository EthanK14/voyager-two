from django.shortcuts import render

# Create your views here.

# main page
def home(request):
    return render(request, "home.html")

def jupiter(request):
    return render(request, "jupiter.html")

def saturn(request):
    return render(request, "saturn.html")

def uranus(request):
    return render(request, "uranus.html")

def neptune(request):
    return render(request, "neptune.html")

def interstellar(request):
    return render(request, "interstellar.html")