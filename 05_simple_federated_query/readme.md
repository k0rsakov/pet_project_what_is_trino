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

## Феде