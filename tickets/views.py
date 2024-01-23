from rest_framework import generics
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from glim_api.permissions import IsOwnerOrReadOnly
from .models import Ticket
from .serializers import TicketSerializer


class TicketList(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Ticket.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     info_serializer = TicketInfoSerializer(queryset)

    #     return Response(dict({"info" : info_serializer.data , "results": serializer.data}))

class TicketDetail(generics.RetrieveAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Ticket.objects.all()
