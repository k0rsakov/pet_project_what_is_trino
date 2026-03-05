# Интеграция Trino в дата-инженерию: Apache Airflow

Минимальная конфигурация Trino для интеграции с Apache Airflow:

```bash
.
├── dags
│   └── simple_trino_example_dag.py
├── docker-compose.yaml
├── Dockerfile
├── handles
│   └── create_connection.py
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

## Создание Trino коннекта в Airflow

Через Web UI:
1) Открыть `Admin`
2) Открыть `Connections`
3) Нажать на `+` (`Add a new record`)
	1) `Connection Id` — `id` подключения
	2) `Connection Type` — `Trino`
	3) `Host` — `trino` (название сервиса в docker-compose)
	4) `Login` — `admin` (любой другой, если авторизация не настроена)
	5) `Port` — `8080` (порт внутри docker-compose)

Через Airflow API:
- Вызвать "_ручку_" — [create_connection.py](handles/create_connection.py) 