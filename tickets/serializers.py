from rest_framework import serializers
from .models import Ticket
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    show_date = serializers.DateTimeField(format="%Y-%m")
    is_owner = serializers.SerializerMethodField()
    seat_row = serializers.SerializerMethodField()
    seat_number = serializers.SerializerMethodField()
    seat_type = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    
    ROWS = ["A", "B", "C", "D", "E", "F", "G"]
    SEAT_PER_ROW = 12

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_seat_row(self, obj):
        row = ROWS[-(self.seat // -SEAT_PER_ROW)]
        return row

    def get_seat_number(self, obj):
        number = self.seat - (SEAT_PER_ROW * (self.seat_row - 1))
        return number

    def get_seat_type(self, obj):
        type = "Plus" if self.seat_row == "G" else "Standard"
        return type

    def get_price(self, obj):
        price = self.movie.price + 10 if self.seat_type == "Plus" else self.movie.price
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
            "is_owner",
            "seat_number",
            "seat_row",
            "seat_type",
            "profile_id",
            "profile_image",
        ]
