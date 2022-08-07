# FOODGRAM

«Продуктовый помощник». Онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

![foodgram-project-react tests](https://github.com/antonysan/foodgram-project-react/actions/workflows/foodgram_workflow.yaml/badge.svg)

## <a name="tech">Технологии</a>

- Python 3.X
- Django 2.2.19
- Docker version 20.10.16
- docker-compose version 1.29.2,

## <a name="install">Установка и запуск</a>

- Скачайте и установите [Python 3.X](https://www.python.org/downloads/), подходящий Вашей операционной системе. Следуйте инструкциям на сайте.
- Скачайте и установите [Docker](https://docs.docker.com/desktop/windows/install/), подходящий Вашей операционной системе. Следуйте инструкциям на сайте.

- Запустите командную строку (терминал)
  - ___Bash___ для пользователей Mac/Linux;
  - ___Git Bash___ для пользователей Windows - при необходимости [скачайте](https://gitforwindows.org/) и установите его.
  
- Запуск контейнера
  - из папки foodgram-project-react/infra необходимо выполнить комманду ```docker-compose up -d --build```
- Далее выполнить миграции, создать суперпользователя и собрать статические файлы
  - ```docker-compose exec backend python manage.py migrate```
  - ```docker-compose exec backend python manage.py createsuperuser```
  - ```docker-compose exec backend python manage.py collectstatic --no-input```

Проект будет доступен по адресу <http://127.0.0.1/admin/>
