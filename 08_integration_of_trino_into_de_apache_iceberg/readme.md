# Интеграция Trino в дата-инженерию: Apache Iceberg

Минимальная конфигурация Trino для интеграции с Apache Iceberg:

```bash
.
├── docker-compose.yaml
├── etc
│   ├── catalog
│   │   ├── iceberg.properties
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

## Пример работы Apache Iceberg в Trino

```sql
SHOW CATALOGS;

DROP SCHEMA IF EXISTS iceberg.test_schema;

CREATE SCHEMA IF NOT EXISTS iceberg.test_schema;

DROP TABLE IF EXISTS iceberg.test_schema.test_table;

CREATE TABLE iceberg.test_schema.test_table (id int, name varchar);

INSERT INTO iceberg.test_schema.test_table VALUES (1, 'Hello Iceberg');

SELECT * FROM iceberg.test_schema.test_table;
```
