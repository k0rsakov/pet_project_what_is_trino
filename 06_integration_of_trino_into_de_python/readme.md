# Интеграция Trino в дата-инженерию: Python

Запуск Trino в Docker:

```yaml
docker-compose up -d
```

Остановка Trino:

```yaml
docker-compose down --remove-orphans
```

С Trino можно работать двумя способами:

1) Через официальное Trino API — [trino](https://pypi.org/project/trino/).
2) Через привычную многим библиотеку SQLAlchemy — [SQLAlchemy](https://pypi.org/project/SQLAlchemy/).

## Demo Trino API

[simple_trino_dbapi_query.py](simple_trino_dbapi_query.py)

## Demo SQLAlchemy

[simple_trino_sqlalchemy_query.py](simple_trino_sqlalchemy_query.py)