from rest_framework import serializers
from .models import Ticket
from movies.models import Movie

from datetime import timedelta
from django.utils import timezone



class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    show_date = serializers.DateField(format="%m/%d/%Y")
    is_owner = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.avatar.url")
    # expired = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    # def get_expired(self, obj):
    #     ticket_time = obj.created_at + timedelta(seconds=30)
    #     current_time = timezone.now()
    #     if ticket_time > current_time: 
    #         return False
    #     else:
    #         return True
        
        
    
    def get_price(self, obj):
        price = obj.movie.price
        return price

    class Meta:
        model = Ticket
        fields = [
            "id",
            "movie",
            "owner",
            "seat",
            "created_at",
            "show_date",
            "reserve",
            "purchased",
            "is_owner",
            "price",
            "profile_id",
            "profile_image",
            # "expired",
        ]

class TicketDetailSerializer(TicketSerializer):
    movie = serializers.ReadOnlyField(source="movie.id")
    show_date = serializers.ReadOnlyField(source="show_date")
    owner = serializers.ReadOnlyField(source="owner")