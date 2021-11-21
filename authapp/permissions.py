from django.contrib.auth import get_user_model
from rest_framework import permissions

from .models import Student


class DefaultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False


class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return int(obj.user.id) == request.user.id
        return False


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        user_id = request.data.get("user", None)
        if request.user.is_authenticated:
            if request.method == "POST":
                try:
                    return request.user.id == int(user_id)
                except:
                    return False
            else:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return int(obj.user.id) == request.user.id

        return False


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            if user.role.name == "student":
                return True
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

