import csv

from django.conf import settings
from django.core.management import BaseCommand
from recipes.models import Ingredient, Tag


class Command(BaseCommand):
    help = 'Creater import data'

    def handle(self, *args, **kwargs):
        data = [
            {
                'name': 'Завтрак',
                'color': '#E26C2D',
                'slug': 'breakfast',
            },
            {
                'name': 'Обед',
                'color': '#49B64E',
                'slug': 'dinner',
            },
            {
                'name': 'Ужин',
                'color': '#8775D2',
                'slug': 'supper',
            }
        ]
        Tag.objects.bulk_create(Tag(**tag) for tag in data)
        self.stdout.write(self.style.SUCCESS('Tags created!'))

        with open(
            f'{settings.BASE_DIR}/data/ingredients.csv',
            'r',
            encoding='utf-8'
        ) as file:
            reader = csv.DictReader(file)
            Ingredient.objects.bulk_create(
                Ingredient(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('ingredients import success'))
