from api.views import (AddDeleteShoppingCart, FavoriteViewSet,
                       IngredientsViewSet, RecipesViewSet, SubcribeViewset,
                       TagsViewSet, TokenViewSet, UsersViewSet, set_password)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('users', UsersViewSet, basename='users')
router.register('tags', TagsViewSet, basename='tags')
router.register('recipes', RecipesViewSet, basename='recipes')
router.register('ingredients', IngredientsViewSet, basename='ingredients')


urlpatterns = [
     path('auth/token/login/',
          TokenViewSet.as_view(),
          name='login'),
     path('users/set_password/',
          set_password,
          name='set_password'),
     path('users/<int:user_id>/subscribe/',
          SubcribeViewset.as_view(),
          name='subscribe'),
     path('recipes/<int:recipe_id>/favorite/',
          FavoriteViewSet.as_view(),
          name='favorite_recipe'),
     path('recipes/<int:recipe_id>/shopping_cart/',
          AddDeleteShoppingCart.as_view(),
          name='shopping_cart'),
     path('', include(router.urls)),
     path('', include('djoser.urls')),
     path('auth/', include('djoser.urls.authtoken')),
]
