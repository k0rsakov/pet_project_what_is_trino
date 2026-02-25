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

## Имена подключений

Каталог регистрируется при создании файла свойств `catalog` в файловой системы `etc/catalog`.

Базовое имя файла устанавливает имя каталога.

Например, предположим, что вы создаете файлы свойств каталогов:

- `etc/catalog/cdh-hadoop.properties`
- `etc/catalog/sales.properties`
- `etc/catalog/web-traic.properties`
- `etc/catalog/mysql-dev.properties`.

После этого каталоги предоставляются в Trino с именами:

- `cdh-hadoop`
- `sales`
- `web-traffic`
- `mysql-dev`

### Как это проверить

Измените имя файла `tpch.properties` на `tpch1.properties` и перезапустите контейнер командой:

```bash
docker-compose restart
```

После этого выполните запрос:

```sql
SHOW CATALOGS;
```

И убедитесь, что каталог `tpch` больше не отображается, а вместо него появился каталог `tpch1`.