# Generated by Django 3.2.14 on 2022-08-06 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favoriterecipe',
            options={'verbose_name': 'Избранный рецепт'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name'], 'verbose_name': 'Ингредиент'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Рецепт'},
        ),
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'ordering': ['-id'], 'verbose_name': 'Количество ингредиента'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ['-id'], 'verbose_name': 'Покупка'},
        ),
        migrations.AlterModelOptions(
            name='subscribe',
            options={'ordering': ['-id'], 'verbose_name': 'Подписка'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id'], 'verbose_name': 'Тэг'},
        ),
    ]
