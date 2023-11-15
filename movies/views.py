from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from glim_api.permissions import ReadOnly
from .models import Movie
from .serializers import MovieSerializer


class MovieList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Movie.objects.annotate(
        likes_count=Count("likes", distinct=True),
        comments_count=Count("comments", distinct=True),
    ).order_by("-created_at")
    filter_backends = [filters.OrderingFilter]
    OrderingFilter = [
        "likes_count",
        "comments_count",
    ]

    def perform_create(self, serializer):
        serializer.save(
            manager=self.request.user, manager_name=self.request.user.username
        )


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]
    queryset = Movie.objects.all()
