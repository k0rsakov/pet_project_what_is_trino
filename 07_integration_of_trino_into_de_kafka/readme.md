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

После создания всей инфраструктуры запускаем её при помощи команды:

```bash
docker compose up -d
```

Затем мы уже можем читать данные из Kafka при помощи Trino.

Самый простой пример чтения:

```sql
SELECT * FROM kafka."default".my_topic LIMIT 1
```

Получим результат:

| _partition_id | _partition_offset | _message_corrupt | _message                                                                                                                                                                                                                                                                         | _headers | _message_length | _key_corrupt | _key | _key_length | _timestamp              |
|---------------|-------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------|--------------|------|-------------|-------------------------|
| 1             | 0                 | false            | {"uuid": "1b3d52e3-aae2-4f99-81ba-9f7a9875e009", "first_name": "\u0418\u0433\u043e\u0440\u044c", "last_name": "\u041a\u0438\u0440\u0438\u043b\u043b\u043e\u0432", "middle_name": "\u0412\u043b\u0430\u0441\u043e\u0432\u0438\u0447", "timestamp": "2026-02-12T11:55:20.996116Z"} | {}       | 272             | false        |      | 0           | 2026-02-12 11:55:20.996 |

Самый простой вариант извлечения ключа:

```sql
SELECT
	JSON_VALUE(_message,'strict $.uuid') AS uuid,
	JSON_VALUE(_message,'strict $.first_name') AS first_name,
	JSON_VALUE(_message,'strict $.last_name') last_name
FROM
	kafka."default".my_topic
```

### Указание модели данных

Одна из основных проблем при работе с Kafka — это соблюдение дата-контрактов и чтение разной модели данных.

Для этого на уровне Trino можно задать конфиг для topic, чтобы его превратить в таблицу.

Для этого создаём папку `kafka` на уровне `catalog` и добавляем туда файл с любым именем, но для консистентности лучше
дать "*продолжение*" каталога.

К примеру, мы назвали свой коннектор как `kafka`и название файла можно сделать `default.my_topic.json`, где `default` —
это схема в каталоге `kafka`, `my_topic` — название таблицы.

Пример `default.my_topic.json`:

```json
{
  "tableName": "my_topic",
  "topicName": "my_topic",
  "schemaName": "default",
  "message": {
    "dataFormat": "json",
    "fields": [
      {
        "name": "uuid",
        "mapping": "uuid",
        "type": "VARCHAR"
      },
      {
        "name": "first_name",
        "mapping": "first_name",
        "type": "VARCHAR"
      },
      {
        "name": "last_name",
        "mapping": "last_name",
        "type": "VARCHAR"
      },
      {
        "name": "middle_name",
        "mapping": "middle_name",
        "type": "VARCHAR"
      },
      {
        "name": "timestamp",
        "mapping": "timestamp",
        "type": "VARCHAR"
      }
    ]
  }
}
```
 
И теперь мы можем перезапустить контейнер Trino командой:
```bash
docker restart trino
```

Мы получим такую структуру папок:

```bash
.
├── docker-compose.yaml
├── etc
│   ├── catalog
│   │   ├── kafka.properties
│   │   └── tpch.properties
│   ├── config.properties
│   ├── jvm.config
│   ├── kafka
│   │   └── default.my_topic.json
│   └── node.properties
├── readme.md
└── simple_producer.py
```