from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if obj == request.user:
            return True

        raise PermissionDenied("Вы не являетесь владельцем этого объекта.")
