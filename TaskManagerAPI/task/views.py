from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task 
from .serializers import TaskSerializer
from .permissions import TaskPermission

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [TaskPermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Task.objects.all()
        elif user.role == 'manager':
            team_users = user.team_members.all()
            return Task.objects.filter(assigned_to__in=team_users) | Task.objects.filter(assigned_to=user)
        else:
            return Task.objects.filter(assigned_to=user)