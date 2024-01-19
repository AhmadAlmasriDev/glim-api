from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()

    def validate_avatar(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size larger than 2MB!")
        if value.image.height > 1500:
            raise serializers.ValidationError("Image height larger than 1500px!")
        if value.image.width > 1500:
            raise serializers.ValidationError("Image width larger than 1500px!")
        return value

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_is_admin(self, obj):
        request = self.context["request"]
        return request.user.is_staff

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "email",
            "about",
            "avatar",
            "is_owner",
            "is_admin",
        ]
