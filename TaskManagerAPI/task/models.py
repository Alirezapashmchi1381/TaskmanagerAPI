from enum import Enum
from django.db import models
from django.conf import settings

class status_enum(str , Enum  ):
    T = 'TODO'
    I = 'IN_PROGRESS'
    R =  'RESOLVED'
    D = 'DONE'

class priority_enum(str , Enum):
    L = 'LOW'
    M = 'MEDIUM'
    H = 'HIGH' 

status_choices = [
    (status.name.title() , status.value) for status in status_enum
]
priority_choices = [
    (priority.name.title() , priority.value) for priority in priority_enum
]


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=1 , choices=status_choices)
    priority = models.CharField(max_length=1 , choices=priority_choices)
    duration = models.DurationField(null=True)#interval in postgresql
    created_at = models.DateTimeField(_auto_now=True)
    updated_at = models.DateTimeField( auto_now_add=True)
    # assigned_to = models.ForeignKey(settings.DEFAULT_USER_AUTHMODEL)

