from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my Portfolio Website!")

def about(request):
    return HttpResponse("About me page.")

def projects(request):
    return HttpResponse("Projects page.")
