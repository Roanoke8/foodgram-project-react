from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TagViewsSet, RecipeViewSet

app_name = 'api'

router = DefaultRouter()

router.register(
    'tags',
    TagViewsSet,
    basename='tags'
)
router.register(
    'recipes',
    RecipeViewSet,
    basename='recipe'
)

urlpatterns = [
    path(
        '',
        include(router.urls)
    )
]
