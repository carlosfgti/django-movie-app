from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    # movies = ', '.join([movie.title for movie in movies])
    # return HttpResponse(movies)
    return render(request, 'movies/index.html', { 'movies': movies })

def detail(request, movie_id):
    # movie = Movie.objects.get(pk=movie_id)
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', { 'movie': movie })