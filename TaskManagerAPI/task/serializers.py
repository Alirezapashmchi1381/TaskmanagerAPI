from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # assigned_to_id = serializers.IntegerField(source = 'assigme_to.id')    
    class Meta:
        model = Task
        fields = ['id' , 'title' , 'description','duration' , 'status' , 'priority' ,'created_at', 'modified_at', 'assigned_to']
        read_only_fields = ['created_at', 'modified_at']

class UpdateTaskSerializer(serializers.ModelSerializer):
    # assigned_to_id = serializers.IntegerField(source = 'assigme_to.id')    
    class Meta:
        model = Task
        fields = ['id' , 'status' , 'priority']
        read_only_fields = ['created_at', 'modified_at']
