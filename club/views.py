from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Club
from .models import Comment

def home(request):
    clubs = Club.objects.all()
    return render(request, 'home.html', {'clubs' : clubs})

def info(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    return render(request, 'info.html', {'club': club})

def add(request):
    if request.method == "POST":
        club = Club()
        club.name = request.POST['name']
        club.detail = request.POST['detail']
        club.members = int(request.POST['members'])
        club.save()
        return redirect('info', club.id)
    return render(request, 'add.html')

def comment(request, club_id):
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.club = get_object_or_404(Club, pk = club_id)
        new_comment.comment = request.POST['comment']
        new_comment.created_at = timezone.now()
        new_comment.save()
    return redirect('info', club_id)

def edit(request, club_id):
    edit_club = Club.objects.get(pk=club_id)
    return render(request, 'edit.html', {'club' : edit_club})

def update(request, club_id):
    update_club = Club.objects.get(pk=club_id)
    update_club.name = request.POST['name']
    update_club.detail = request.POST['detail']
    update_club.members = int(request.POST['members'])
    update_club.save()
    return redirect('info', update_club.id)    

def delete(request, club_id):
    delete_club = Club.objects.get(pk = club_id)
    delete_club.delete()
    return redirect(home)
    

