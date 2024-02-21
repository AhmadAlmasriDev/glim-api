from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    owner_name = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_avatar = serializers.ReadOnlyField(
        source="owner.profile.avatar.url")
    approved = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            "id",
            "movie",
            "owner",
            "owner_name",
            "profile_id",
            "profile_avatar",
            "created_at",
            "updated_at",
            "comment_body",
            "approved",
            "is_owner",
        ]


class CommentDetailSerializer(CommentSerializer):
    movie = serializers.ReadOnlyField(source="movie.id")
    owner = serializers.ReadOnlyField(source="owner.id")
