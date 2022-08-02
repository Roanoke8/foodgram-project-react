from rest_framework import serializers
from recipe.models import Tag, Recipe, Ingridients
from drf_base64.fields import Base64ImageField
from users.serializers import UserDetailSerialisers


class IngridientsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Ingridients


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'color', 'slug')
        model = Tag


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        required=True,
        # source='recipe'
        queryset=Ingridients.objects.all()
    )
    author = UserDetailSerialisers(
        read_only=True
    )
    image = Base64ImageField(
        max_length=None,
        use_url=True
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )
    cooking_time = serializers.IntegerField()
    is_favorited = serializers.BooleanField(
        read_only=True
    )
    is_in_shopping_cart = serializers.BooleanField(
        read_only=True
    )

    class Meta:
        fields = ('__all__')
        model = Recipe

    def validate_cooking_time(self, cooking_time):
        if int(cooking_time) < 1:
            raise serializers.ValidationError(
                'Время приготовления должно быть больше 0')
        return cooking_time


