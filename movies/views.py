from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from movies.serializers import MovieSerializer, SessionSerializer
from movies.models import Movie, Session


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny,)


class SessionListView(ListAPIView):
    serializer_class = SessionSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        movie_id = self.kwargs.get('movie_id')
        movie = get_object_or_404(Movie, id=movie_id)
        session = Session.objects.filter(movie=movie)
        return session
