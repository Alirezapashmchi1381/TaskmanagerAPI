from django.db import models
from django.conf import settings
from .enums import status_enum , priority_enum 

status_choices = [
    (status.name.title() , status.value) for status in status_enum
]

priority_choices = [
        (priority.name.title() , priority.value) for priority in priority_enum
]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    status = models.CharField(max_length=10 ,choices=status_choices)
    priority = models.CharField(max_length=10 , choices=priority_choices)
    created_at = models.DateTimeField(auto_now=True )
    modified_at = models.DateTimeField(auto_now_add=True  )
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)