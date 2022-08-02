from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators


User = get_user_model()


class Units(models.Model):
    title = models.CharField(
        'Единицы измерения',
        max_length=128
    )

    def __str__(self):
        return f'{self.title}'


class Tag(models.Model):
    title = models.CharField(
        'Название Тега',
        max_length=200,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )
    color = models.CharField(
        'Цвет',
        max_length=7,
        unique=True)


class Ingridients(models.Model):
    title = models.CharField(
        'Название ингридиента',
        max_length=256
    )
    units = models.CharField(
        'мера измерения',
        max_length=256
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        validators=(
            validators.MinValueValidator(
                1, message='Мин. количество ингридиентов 1'),),
        verbose_name='Количество',)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        unique_together = ['user', 'author']

    def __str__(self):
        return self.author.username


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Автор',
    )
    name = models.CharField(
        'Название рецепта',
        max_length=255,
    )
    image = models.ImageField(
        'Изображение рецепта',
        upload_to='static/recipe/',
        blank=True,
        null=True,
    )
    text = models.TextField(
        'Описание рецепта',
    )
    cooking_time = models.BigIntegerField(
        'Время приготовления рецепта',
    )
    ingredients = models.ManyToManyField(
        Ingridients,
        related_name='RecipeIngredient',
        verbose_name='Ингридиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        validators=[
            validators.MinValueValidator(
                1,
                message='Мин. время приготовления 1 минута'
            ),
        ]
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )


class FavoriteRecipe(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_recipe',
    )
    recipe = models.ManyToManyField(
        Recipe,
        related_name='favorite_recipe',
    )


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='cart',

    )

    class Meta:
        unique_together = ['user', 'recipe']
