from rest_framework import serializers
from .models import Movie
from likes.models import Like
from movies.models import RATING


class MovieSerializer(serializers.ModelSerializer):
    manager = serializers.ReadOnlyField(source="manager.username")
    manager_name = serializers.ReadOnlyField()
    is_admin = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    start_date = serializers.DateField(format="%m/%d/%Y")
    end_date = serializers.DateField(format="%m/%d/%Y")
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

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

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, movie=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "trailer",
            "manager",
            "manager_name",
            "created_at",
            "updated_at",
            "start_date",
            "end_date",
            "session_time",
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
            "like_id",
            "likes_count",
            "comments_count",
        ]


class MovieServiceSerializer(serializers.ModelSerializer):

    service = serializers.SerializerMethodField()

    def get_service(self, obj):
        ratings = []
        for item in RATING:
            ratings.append(item[1])
        info = {"ratings": ratings}
        return info

    class Meta:
        model = Movie
        fields = [
            "service",
        ]
