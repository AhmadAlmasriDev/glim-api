from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    manager = serializers.ReadOnlyField(source="owner.username")
    manager_name = serializers.ReadOnlyField(source="manager_name")
    is_admin = serializers.SerializerMethodField()

    def get_is_admin(self, obj):
        request = self.context["request"]
        return request.user.is_staff

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "manager",
            "manager_name",
            "created_at",
            "updated_at",
            "rated",
            "year",
            "director",
            "genre",
            "distribution",
            "actors",
            "poster",
            "discreption",
            "price",
            "status",
            "is_admin",
        ]
