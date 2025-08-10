from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import role_enum

role_choices = [
    (role.name.title() , role.value) for role in role_enum
]

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=role_choices, default='user')
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='team_members')
