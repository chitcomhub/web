# Chechen IT Community

## Третья попытка

Впервые мы решили отказаться от Django и сделать сайт на чем-то более легком.

## Запуск проекта на production компьютере:
1) клонируем репо: ``git clone ...``
2) заходим в главую папку: ``web``
3) если на Windows, то проверяем что "Docker Desktop" вклучен
4) запускаем `docker-compose up`
5) фронт-енд можно посмотрет открыв веб-браузер и зайдя на: `localhost:80`
6) бэк-енд у  нас находится тут: `localhost:8000`


автогенерация миграции для alembic
```shell
alembic revision --autogenerate -m "Init"
```

автогенерация миграции для alembic
```shell
alembic revision --autogenerate -m "Init"
```