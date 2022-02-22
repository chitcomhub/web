# Chechen IT Community 

[![front-status]][actions-link]

## Третья попытка

Впервые мы решили отказаться от Django и сделать сайт на чем-то более легком.

## Установка проекта к себе:
1) клонируем репо: ``git clone ...``
2) заходим в главную папку: ``web``
3) если на Windows, то проверяем что "Docker Desktop" включен
4) запускаем `docker-compose up`
5) фронт-енд можно посмотреть открыв веб-браузер и зайдя на: `localhost:80`
6) бэк-енд у нас находится тут: `localhost:8000`


автогенерация миграций для alembic
```shell
alembic revision --autogenerate -m "Init"
```

#### [Гайд для новичков][contributing-guide]

[contributing-guide]: https://docs.google.com/document/u/0/d/1e7mNb46DegS5nOsWPrilzj8Q2rCkB5cLIdXK8Hs97xs/mobilebasic
[actions-link]: https://github.com/chitcomhub/web/actions
[front-status]: https://github.com/chitcomhub/web/workflows/chitweb-frontend/badge.svg
