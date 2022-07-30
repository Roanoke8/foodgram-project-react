from django.contrib import admin

from .models import Units, Tag, Ingridients, Follow, Recipe, FavoriteRecipe, Cart


@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',)
    list_editable = ('title',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'color', )
    search_fields = ('title',)
    empty_value_display = '-пусто-'

@admin.register(Ingridients)
class IngridientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'units', 'amount', )
    empty_value_display = '-пусто-'

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

@admin.register(Cart)
class CartRecipeAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

