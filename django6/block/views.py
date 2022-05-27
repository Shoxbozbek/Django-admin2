from django.shortcuts import render
from .models import Home


def home(request):
   
    py = Home.objects.all()
    extend = {
        "home":py
    }
    
    return render(request, 'home.html', extend)


def about(request):
    return render(request, 'about.html')