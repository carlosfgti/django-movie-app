from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    movies = ', '.join([movie.title for movie in movies])
    return HttpResponse(movies)