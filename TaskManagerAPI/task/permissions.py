from rest_framework.permissions import BasePermission, SAFE_METHODS

class TaskPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        if user.role == 'admin':
            return True

        if user.role == 'manager' and request.method in ['GET', 'POST']:
            return True

        if request.method in SAFE_METHODS:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == 'admin':
            return True

        if user.role == 'manager':
            return obj.assigned_to.manager == user

        if user == obj.assigned_to and request.method in SAFE_METHODS:
            return True

        return False
