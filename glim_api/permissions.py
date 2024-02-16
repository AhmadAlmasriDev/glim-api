from rest_framework.permissions import BasePermission, SAFE_METHODS
from datetime import datetime, timedelta

from django.utils import timezone


"""
Permission current user is the owner of the obj, if not then read only
"""


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


"""
Permission current user is the owner of the obj,
if not then read only until the obj expires (3 min) after that give permission
"""


class IsOwnerOrReadOnlyOrExpired(BasePermission):

    def object_expired(self, obj):
        ticket_time = obj.created_at + timedelta(seconds=3*60)
        current_time = timezone.now()
        return ticket_time < current_time

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if self.object_expired(obj) or obj.owner == request.user:
            return True
        else:
            return False


"""
Permission read only
"""


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
