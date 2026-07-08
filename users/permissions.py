from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True

        elif request.user.role == 'user':
            return False

        return obj.id == request.user.id