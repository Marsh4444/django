from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def projects(request):
    return render(request, "main/projects.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #still have to debug this soon
            Contact.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"]
            )
            return redirect("contact_success")
    else:
        form = ContactForm()
    
    return render(request, "main/contact.html", {"form": form})

def contact_success(request):
    return render(request, "main/contact_success.html")
