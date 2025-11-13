from django.shortcuts import render, get_object_or_404, redirect
from .models import Film

def home(request):
    films = Film.objects.all()
    return render(request, 'home.html', {'films': films})

def detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    return render(request, 'detail.html', {'film': film})