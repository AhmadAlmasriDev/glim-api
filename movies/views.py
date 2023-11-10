from django.http import Http404
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from glim_api.permissions import ReadOnly

class MovieList(APIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser|ReadOnly]

    def get(self, request):
        movies = Movie.objects.all()
        serilalizer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serilalizer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(manager=request.user, manager_name=request.user.username)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            self.check_object_permissions(self.request, movie)
            return movie
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(
            movie, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
