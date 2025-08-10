from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.mixins import CreateModelMixin
from .models import Task 
from .serializers import TaskSerializer , UpdateTaskSerializer
from .permissions import TaskPermission

class TaskViewSet(ModelViewSet):
    permission_classes = [TaskPermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'Admin':
            return Task.objects.all()
        elif user.role == 'Manager':
            team_users = user.team_members.all()
            return Task.objects.filter(assigned_to__in=team_users) | Task.objects.filter(assigned_to=user)
        else:
            return Task.objects.filter(assigned_to=user)
        
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return UpdateTaskSerializer
        return TaskSerializer