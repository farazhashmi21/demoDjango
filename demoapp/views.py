from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "demo/index.html")

def about(request):
    return render(request, "demo/about.html")

def services(request):
    return render(request, "demo/services.html")

def contact(request):
    return render(request, "demo/contact.html")
