import os
from csv import DictReader
from venv import create

from django.core.management import BaseCommand
from recipe.models import Ingridients


class Command(BaseCommand):
    """Загрузка данных в таблицу Category.
    Можно указать путь к csv-файлу. Если путь не указан,
    загрузка выполняется из DEFAULT_FILE_PATH.
    """

    DEFAULT_FILE_PATH = os.path.join(
        os.path.join(os.path.abspath('../../'), 'data'),
        'ingredients.csv'
    )

    help = 'Загружает данные из csv-файла в таблицу Category.'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', type=str, nargs='?', default=self.DEFAULT_FILE_PATH
        )

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, encoding='utf-8') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                create = Ingridients.objects.create(
                    id=row['id'],
                    title=row['name'],
                    units=row['units']
                )

            # for row in reader:
                # print(row['id'], row['name'], row['units'])
            #     _, created = Ingridients.objects.create(
            #         # id=1,
            #         title='name',
            #         units='asd',
            #     )
        self.stdout.write(
            self.style.SUCCESS(
                f'Данные из {file_path} успешно загружены.'
            )
        )