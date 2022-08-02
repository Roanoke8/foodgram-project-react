from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


User = get_user_model()


class UserListSerialisers(serializers.ModelSerializer):
    # is_subscribed = serializers.BooleanField(read_only=True)

    class Meta:
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            # 'is_subscribed',
            'password'
        )
        model = User


class UserDetailSerialisers(serializers.ModelSerializer):

    class Meta:
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            # 'is_subscribed',
            'password'
        )
        model = User


class TokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label='Email',
        write_only=True)
    password = serializers.CharField(
        label='Пароль',
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True)
    token = serializers.CharField(
        label='Токен',
        read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = get_object_or_404(
                User,
                email=email,
                password=password
            )
        attrs['user'] = user
        return attrs
