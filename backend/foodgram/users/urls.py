from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserListViewSet, AuthTokenViewSet

app_name = 'users'

router = DefaultRouter()

router.register(
    'users',
    UserListViewSet,
    basename='users_list'
)

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),
    path(
        'auth/token/login/',
        AuthTokenViewSet.as_view(),
        name='login'
    ),
    path(
        '',
        include('djoser.urls')
    ),
    path(
        'auth/',
        include('djoser.urls.authtoken')
    ),
]
