# Интеграция Trino в дата-инженерию: Kafka

Минимальная конфигурация Trino для интеграции с Kafka:

```bash
.
├── docker-compose.yaml
├── etc
│   ├── catalog
│   │   ├── kafka.properties
│   │   └── tpch.properties
│   ├── config.properties
│   ├── jvm.config
│   └── node.properties
├── readme.md
└── simple_producer.py
```

Запуск Trino в Docker:

```yaml
docker-compose up -d
```

Остановка Trino:

```yaml
docker-compose down --remove-orphans
```

## Взаимодействие с Kafka

[Kafka Web UI](http://localhost:8088/)

Для записи данных в topic `my_topic` необходимо запустить файл — [simple_producer.py](simple_producer.py)

## Взаимодействие с Kafka через Trino

