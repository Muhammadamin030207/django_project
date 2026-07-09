from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and
            request.user.role in ['admin', 'seller', 'super_admin']
        )
    
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False