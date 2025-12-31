from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), #views.home → run the home function
    path('about/', views.about, name='about'), #name → label for later use (links)
    path('projects/', views.projects, name='projects'), 
]