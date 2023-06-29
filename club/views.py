from django.shortcuts import render, redirect
from .models import Club

def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info.html')

def add(request):
    if request.method == "POST":
        club = Club()
        club.name = request.POST['name']
        club.detail = request.POST['detail']
        club.members = request.POST['members']
        club.save()
        return redirect('info', club.id)
    return render(request, 'add.html')

# Create your views here.
