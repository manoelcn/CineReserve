from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    duration = models.IntegerField()
    banner = models.URLField()

    def __str__(self):
        return self.title


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    room = models.CharField(max_length=100)
    session_datetime = models.DateTimeField()
    total_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie.title} -  {self.session_datetime}"
