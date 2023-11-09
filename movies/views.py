from django.http import Http404
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer


class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serilalizer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serilalizer.data)



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
        serializer = ProfileSerializer(
            movie, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
