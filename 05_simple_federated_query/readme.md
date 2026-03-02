# Простой федеративный запрос в Trino в Docker

Минимальная конфигурация Trino:

```bash
.
├── docker-compose.yaml
├── etc
│   ├── catalog
│   │   ├── postgresql.properties
│   │   └── tpch.properties
│   ├── config.properties
│   ├── jvm.config
│   └── node.properties
└── readme.md
```

Запуск Trino в Docker:

```yaml
docker-compose up -d
```

Остановка Trino:

```yaml
docker-compose down --remove-orphans
```

## Федеративный запрос

После того как вы развернули сервисы, выполните запрос для просмотра текущих каталогов:

```sql
SHOW CATALOGS;
```

Затем выполните команду на создание таблицы в PostgreSQL используя наш коннектор `postgresql.properties`:

```sql
CREATE TABLE postgresql.public.foo (id bigint, value bigint);
```

Теперь вы можете проверить наличие данной таблицы в PostgreSQL командой:

```sql
SHOW TABLES FROM postgresql.public;
```

И теперь вы можете выполнить операцию вставки данных в неё данные командой:

```sql
INSERT INTO postgresql.public.foo VALUES(1, 42);
```

Посмотреть результат своих действий используйте команду:

```sql
SELECT * FROM postgresql.public.foo;
```

И сейчас можно посмотреть как Trino работает с федеративными запросами, для этого выполните команду:

```sql
SELECT
	customer.custkey AS tpch_id,
	pg.value AS foo_value
FROM tpch.sf1.customer AS customer
	JOIN postgresql.public.foo AS pg
		ON customer.custkey = pg.id
WHERE 1=1
```
