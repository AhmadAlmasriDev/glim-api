from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    manager = serializers.ReadOnlyField(source="manager.username")
    manager_name = serializers.ReadOnlyField()
    is_admin = serializers.SerializerMethodField()

    def validate_poster(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size larger than 2MB!")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height larger than 4096px!")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width larger than 4096px!")
        return value

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
