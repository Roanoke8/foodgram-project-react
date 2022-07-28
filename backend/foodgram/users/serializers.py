from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListSerialisers(serializers.BaseSerializer):
    is_subscribed = serializers.BooleanField(read_only=True)

    class Meta:
        fields = (
            'email', 'id', 'username',
            'first_name', 'last_name', 'is_subscribed')
        model = User
