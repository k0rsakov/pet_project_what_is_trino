# Простой запуск Trino в Docker без конфигурации

> В данном примере Не будут тестовые каталоги.

Минимальная конфигурация Trino:

```bash
.
├── docker-compose.yaml
├── etc
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
