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

## Чтение

- Чтение через Trino API — [simple_trino_dbapi_select_query.py](simple_trino_dbapi_select_query.py)
- Чтение через SQLAlchemy — [simple_trino_sqlalchemy_select_query.py](simple_trino_sqlalchemy_select_query.py)

## Запись

- Запись через Trino API — [simple_trino_dbapi_dml_query.py](simple_trino_dbapi_dml_query.py)
- Запись через SQLAlchemy — [simple_trino_sqlalchemy_dml_query.py](simple_trino_sqlalchemy_dml_query.py)

## Note

При работе с Trino через SQLAlchemy в движке (`uri`) необходимо указывать полный путь до таблицы.

Пример оформления `uri`:

```python
from sqlalchemy import create_engine

connection_uri = f"trino://{TRINO_USER}@{TRINO_HOST}:{TRINO_PORT}/{TRINO_CATALOG}/{TRINO_SCHEMA}"
engine = create_engine(connection_uri)
```

Поэтому в демо так:

```python
engine = create_engine('trino://admin@localhost:8080/memory/default')
```
