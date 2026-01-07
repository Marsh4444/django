from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def projects(request):
    return render(request, "main/projects.html")

def contact(request):
    return render(request, "main/contact.html")
