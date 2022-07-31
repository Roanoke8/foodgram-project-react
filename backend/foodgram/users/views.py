from .serializers import UserListSerialisers, TokenSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.hashers import make_password


from django.contrib.auth import get_user_model

User = get_user_model()


class UserListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerialisers
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    @action(
        detail=False,
        permission_classes=[IsAuthenticated],
        methods=['GET'],
        url_path='me',
    )
    def me(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class AuthTokenViewSet(ObtainAuthToken):
    """Авторизация пользователя."""

    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'Token': token.key
            },
            status=status.HTTP_201_CREATED
        )
