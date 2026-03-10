# Простой запуск Trino cluster в Docker

Минимальная конфигурация Trino cluster:

```bash
.
├── coordinator
│   └── etc
│       ├── catalog
│       │   └── tpch.properties
│       ├── config.properties
│       ├── jvm.config
│       └── node.properties
├── docker-compose.yaml
├── readme.md
├── worker-1
│   └── etc
│       ├── catalog
│       │   └── tpch.properties
│       ├── config.properties
│       ├── jvm.config
│       └── node.properties
└── worker-2
    └── etc
        ├── catalog
        │   └── tpch.properties
        ├── config.properties
        ├── jvm.config
        └── node.properties
```

Запуск Trino cluster в Docker:

```yaml
docker-compose up -d
```

Остановка Trino cluster:

```yaml
docker-compose down --remove-orphans
```

Самый простой запрос к Trino cluster:

```sql
SELECT * FROM system.runtime.nodes;
```

Должен вывести:

| node_id            | http_uri               | node_version | coordinator | state  |
|--------------------|------------------------|--------------|-------------|--------|
| coordinator-node-1 | http://172.20.0.3:8080 | 479          | true        | active |
| worker-node-2      | http://172.20.0.4:8080 | 479          | false       | active |
| worker-node-1      | http://172.20.0.2:8080 | 479          | false       | active |

Trino WEB UI: http://localhost:8080/ui/

Запрос в Trino cluster к каталогу `tpch`:

```sql
EXPLAIN ANALYZE VERBOSE
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

И вы получите план запроса на Trino cluster.

Явные атрибуты, которые указывают на то, что запрос выполняется на кластере, включают:
- `Tasks count: 2`
- `Task output distribution: {}`
- `Task input distribution: {}`
- `'CPU time distribution (s)' = {}`
- `'Input rows distribution' = {}`
- `'Scheduled time distribution (s)' = {}`
- `RemoteSource[sourceFragmentIds = [2]]`
