# Простой запуск Trino в Docker c использованием конфигурации и своего коннектора

Минимальная конфигурация Trino:

```bash
.
├── docker-compose.yaml
├── etc
│   ├── catalog
│   │   └── tpch.properties
│   ├── config.properties
│   ├── jvm.config
│   └── node.properties
├── LICENSE
└── README.md
```

Запуск Trino в Docker:

```yaml
docker-compose up -d
```

Остановка Trino:

```yaml
docker-compose down --remove-orphans
```

Самый простой запрос к Trino:

```sql
SHOW CATALOGS;
```


Теперь мы снова можем обращаться к каталогу `tpch` и выполнять запросы к нему.

Самый простой запрос к каталогу `tpch` в Trino:

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