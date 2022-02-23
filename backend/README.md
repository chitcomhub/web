# Backend

#### Миграции для alembic

```shell
alembic revision --autogenerate -m "Init"
```

***

#### Запуск тестов

Открываем контейнер где расположен Backend. Вне контейнера не получиться - не сможем получить доступ к БД.

```shell
docker exec -ti <container name> /bin/bash
```

Запускаем тесты

```shell
pytest
```

