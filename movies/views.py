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
        self.queryset = Session.objects.filter(movie_id=movie_id)
        return self.queryset
