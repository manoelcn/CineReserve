from django.contrib import admin
from movies.models import Movie, Session


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'duration')
    search_fields = ('title',)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'room', 'session_datetime', 'total_seats')
