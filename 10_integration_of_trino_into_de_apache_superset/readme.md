# Интеграция Trino в дата-инженерию: Apache Superset

Минимальная конфигурация Trino для интеграции с Apache Superset:

```bash

```

Запуск Trino в Docker:

```yaml
docker-compose up -d
```

Остановка Trino:

```yaml
docker-compose down --remove-orphans
```

## Создание Trino коннекта в Superset

Через Web UI:
1) Открыть `Settings`
2) Открыть `Database connections`
3) Нажать `+ Database`
4) Выбрать в коннектах `Trino`
5) Указать `SQLAlchemy URI` -> `trino://admin@trino:8080`

### Тонкости работы с коннекторами в Superset
Один из основных моментов, что классический Superset настроен под "*классические*" БД и поэтому он предполагает структуру:
- `database`
- `schema`
- `table`

Но так как в Trino другая структура, то при написании запросов в SQL Lab, он отображает наш коннект как `database` и отображает схемы "*дефолтные*" `schema` (`SHOW SCHEMAS;`):

| Schema             |
| ------------------ |
| information_schema |
| jdbc               |
| metadata           |
| runtime            |

Но если написать запрос, который позволит посмотреть на схемы в классическом коннекторе `tpch`:
```sql
SHOW SCHEMAS from tpch
```
То он выведет следующую структуру:

| Schema             |
| ------------------ |
| information_schema |
| sf1                |
|sf100|
|sf1000|
|sf10000|
|sf100000|
|sf300|
|sf3000|
|sf30000|
|tiny|

Поэтому классические запросы к `tpch` будут работать без проблем:
```sql
SELECT
  orderdate,
  count(orderKey) AS cnt_orders,
  sum(totalprice) AS sum_orders
FROM
  tpch.sf1.orders
WHERE
  1=1
GROUP BY
  1;
```

___

Поэтому все коннекторы будут работать по тому же принципу. Если создать коннектор в Trino как описано в [05_simple_federated_query](../05_simple_federated_query) и создать таблицу в PostgreSQL:
```sql
CREATE TABLE foo (id int8 PRIMARY KEY, value int8);

INSERT INTO foo VALUES(1,42);
```

То после перезагрузки сервисов можно выполнить запрос в Superset:
```sql
SELECT * from postgresql.public.foo
```

И получить результат:

| id  | value |
| --- | ----- |
| 1   | 42    |

___

Можно указывать конкретный коннектор в Superset при помощи чёткого указания его в `SQLAlchemy URI`.

Пример настройки `SQLAlchemy URI`:

```python
trino://admin@trino:8080/memory/default
```

```python
trino://<username>:<password>@<host>:<port>/<catalog>/<schema>
```

| Часть URI  | Значение     | Почему                                              |
| ---------- | ------------ |-----------------------------------------------------|
| `trino://` | Протокол     | Драйвер Trino                                       |
| `admin`    | Пользователь | Trino по умолчанию принимает любого                 |
| `trino`    | Хост         | Имя сервиса из `docker-compose.yaml`                |
| `8080`     | Порт         | Стандартный порт Trino                              |
| `memory`   | Каталог      | Замени на свой каталог (например `hive`, `iceberg`) |
| `default`  | Схема        | Замени на нужную схему                              |

Если взять за пример прошлый коннектор к PostgreSQL, то создаём такой `SQLAlchemy URI`:

```python
trino://admin@trino:8080/postgresql
```

Называем его как `Trino_PG` и уже в SQL Lab выбираем коннект `Trino_PG` и пишем запрос:
```sql
SELECT * from public.foo
```

И получаем тот же результат:

| id  | value |
| --- | ----- |
| 1   | 42    |

И также теперь Superset корректно видит модель данных и схемы коннектора, потому что мы сделали подключение "*к Database*" через Trino и для Superset это классическая база данных, где у нас есть `schema` -> `table`