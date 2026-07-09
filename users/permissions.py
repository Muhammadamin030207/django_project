from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role in ["admin", "super_admin"]
        )

    def has_object_permission(self, request, view, obj):
        return request.user.role in ["admin", "super_admin"]


class IsSuperAdminUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "super_admin"
        )

    def has_object_permission(self, request, view, obj):
        return request.user.role == "super_admin"