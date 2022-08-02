

from .serializers import TagSerializer, RecipeSerializer
from .permissions import IsAuthorOrAdminOrReadOnly
from recipe.models import Tag, Recipe
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated

class TagViewsSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrAdminOrReadOnly, )


    def perform_create(self, serializer):
        """Добавляет пользователя в качестве автора рецепта."""
        serializer.save(author=self.request.user)