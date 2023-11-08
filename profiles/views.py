from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfilesSerializer


class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serilalizer = ProfilesSerializer(profiles, many=True)
        return Response(serilalizer.data)
