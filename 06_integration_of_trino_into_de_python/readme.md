# Простой запуск Trino в Docker без конфигурации

> В данном примере будут тестовые каталоги:
> - jmx
> - memory
> - system
> - tpcds
> - tpch 

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
