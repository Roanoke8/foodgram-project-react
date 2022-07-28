from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet, AuthToken

app_name = 'users'

router = DefaultRouter()

router.register('users', UsersViewSet)




urlpatterns = [
    path("auth/", include("djoser.urls.authtoken")),
    path('', include(router.urls)),
    path('auth/token/login/', AuthToken.as_view(),name='login'),
]
