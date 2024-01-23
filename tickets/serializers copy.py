from rest_framework import serializers
from .models import Ticket, SEATS
from movies.models import Movie


# ROWS = ["A", "B", "C", "D", "E", "F", "G"]
# SEAT_PER_ROW = 12


class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    show_date = serializers.DateTimeField(format="%m/%d/%Y")
    is_owner = serializers.SerializerMethodField()
    seats = serializers.SerializerMethodField()
    # seat_row = serializers.SerializerMethodField()
    # seat_number = serializers.SerializerMethodField()
    # seat_type = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.avatar.url")

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_seats(self, obj):
        return SEATS
    

    # def get_seat_row(self, obj):
    #     row = ROWS[-(obj.seat // -SEAT_PER_ROW) - 1]
    #     return row

    # def get_seat_number(self, obj):
    #     number = obj.seat - (SEAT_PER_ROW * (-(obj.seat // -SEAT_PER_ROW) - 1))
    #     return number

    # def get_seat_type(self, obj):
    #     type = "Plus" if self.get_seat_row(obj) == "G" else "Standard"
    #     return type

    # def get_price(self, obj):
    #     price = (
    #         obj.movie.price + 10
    #         if self.get_seat_type(obj) == "Plus"
    #         else obj.movie.price
    #     )
    #     return price

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
            "is_owner",
            "seats",
            # "seat_number",
            # "seat_row",
            # "seat_type",
            "price",
            "profile_id",
            "profile_image",
        ]

    # def to_representation(self, instance):
    #     output = super().to_representation(instance)
    #     response_dict = dict()
    #     response_dict[info]={}
    #     response_dict[results]=output
        
    #     return response_dict

    # def to_internal_value(self, obj):
    #     resource_data = data['results']

    #     return super().to_internal_value(resource_data)

   




    # def to_representation(self, instance):

    #     output = super().to_representation(instance)

        

    #     return { 'info' : SEATS, "results"  : output}