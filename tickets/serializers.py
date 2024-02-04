from rest_framework import serializers
from .models import Ticket
from movies.models import Movie


class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    show_date = serializers.DateField(format="%m/%d/%Y")
    is_owner = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.avatar.url")

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner
    
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
        ]

class TicketDetailSerializer(TicketSerializer):
    movie = serializers.ReadOnlyField(source="movie.id")
    show_date = serializers.ReadOnlyField(source="show_date")
    owner = serializers.ReadOnlyField(source="owner")