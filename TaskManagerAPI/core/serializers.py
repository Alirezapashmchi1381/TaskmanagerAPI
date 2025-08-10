from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .enums import role_enum

User = get_user_model()
role_choices = [
    (role.name.title() , role.value) for role in role_enum
]
class UserCreateSerializer(BaseUserCreateSerializer):
        role = serializers.ChoiceField(choices=role_choices)

        class Meta(BaseUserCreateSerializer.Meta):
            model = User
            fields = tuple(BaseUserCreateSerializer.Meta.fields) + ('role','manager')

