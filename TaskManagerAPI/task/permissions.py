from rest_framework.permissions import BasePermission, SAFE_METHODS

class TaskPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.role == 'Admin':
            return True
        if user.role == 'Manager':
            return request.method in ['POST' , 'GET' , 'PUT' , 'DELETE']
        if user.role == 'User':
            return request.method in [ 'GET' , 'PUT']



    # def has_object_permission(self, request, view, obj):
    #     user = request.user

    #     if request.method in SAFE_METHODS:
    #         if user.role == "Admin":
    #             return True
    #         elif user.role == "Manager":
    #             return obj.assigned_to in self.get_manager_allowed_users(user)
    #         elif user.role == "User":
    #             return obj.assigned_to == user
    #     return False

    # def get_manager_allowed_users(self, user):
    #     return user.team_members.all()  