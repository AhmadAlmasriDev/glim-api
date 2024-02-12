from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from glim_api.permissions import IsOwnerOrReadOnly
from .models import Ticket
from .serializers import TicketSerializer, TicketDetailSerializer


class TicketList(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Ticket.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields =[
        'movie',
        'show_date',
        'owner',
        
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Ticket.objects.all()
