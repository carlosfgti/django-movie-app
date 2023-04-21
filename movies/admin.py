from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    exclude = ('created_at', '')

class MovieAdmin(admin.ModelAdmin):
    # fields = ('title')
    exclude = ('created_at', '')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
