# Что такое Trino

- ✉️ Вопросы, обучение, консультации по Data Engineering — пиши в
  личку: https://korsak0v.notion.site/Data-Engineer-185c62fdf79345eb9da9928356884ea0
- 💥 Аналог Notion (если не работает ссылка выше) — https://www.dataengineers.pro/mentors/korsakov-ivan
- [Видео](https://youtu.be/Z2k-b7ALuuM) — https://youtu.be/Z2k-b7ALuuM

## О видео

🔥 Хочешь понять, что такое Trino (ex-PrestoSQL), как с его помощью делать федеративные запросы к разным источникам
данных одновременно и почему его так любят в Data Engineering? В этом [видео](https://youtu.be/Z2k-b7ALuuM) разберём
Trino с нуля на живых примерах: от локального запуска в Docker до полноценной интеграции с PostgreSQL, Apache Kafka,
Apache Iceberg, Airflow и Superset.

🗂️ GitHub репозиторий с кодом: https://github.com/k0rsakov/pet_project_what_is_trino

✉️ Вопросы, обучение, консультации по Data Engineering — пиши в
личку: https://korsak0v.notion.site/Data-Engineer-185c62fdf79345eb9da9928356884ea0

💥 Аналог Notion (если не работает ссылка выше) — https://www.dataengineers.pro/mentors/korsakov-ivan

💡 В конце видео — практические рекомендации: разбираем специфику и тонкости работы с Trino, чтобы вы могли эффективно
использовать его для аналитики и избегать популярных ошибок при проектировании Data-платформы.

Таймкоды:
- 00:00 — начало
- 00:52 — Теория по Trino
- 04:31 — Простой запуск Trino в Docker без конфигурации
- 06:35 — Простой запуск Trino в Docker c использованием конфигурации
- 08:00 — Простой запуск Trino в Docker c использованием конфигурации и своего коннектора
- 10:56 — Простой запуск Trino cluster в Docker
- 16:59 — Простой федеративный запрос в Trino в Docker
- 20:31 — Интеграция Trino в дата-инженерию: Python
- 25:28 — Интеграция Trino в дата-инженерию: Kafka
- 29:42 — Интеграция Trino в дата-инженерию: Apache Iceberg
- 33:30 — Интеграция Trino в дата-инженерию: Apache Airflow
- 39:55 — Интеграция Trino в дата-инженерию: Apache Superset
- 46:20 — Тонкости Trino и заключение

## О проекте

Оглавление:

- [00_the_theory_of_trino](00_the_theory_of_trino) — Теория по Trino:
  - [01_what_is_tirno.md](00_the_theory_of_trino/01_what_is_tirno.md) — Что такое Trino
  - [02_what_is_trino_cluster.md](00_the_theory_of_trino/02_what_is_trino_cluster.md) — Что такое Trino Cluster
  - [03_subtleties_of_the_trino.md](00_the_theory_of_trino/03_subtleties_of_the_trino.md) — Тонкости при работе с Trino
- Быстрые старты:
    - [01_simple_trino_setup](01_simple_trino_setup) — Запуск Trino без конфигурации.
    - [02_simple_trino_setup_with_configuration](02_simple_trino_setup_with_configuration) — Запуск Trino со своей
      конфигурацией.
    - [03_simple_trino_with_connector](03_simple_trino_with_connector) — Запуск Trino с указанием коннектора к
      источнику.
    - [04_simple_trino_cluster](04_simple_trino_cluster) — Запуск Trino Cluster.
    - [05_simple_federated_query](05_simple_federated_query) — Запуск Trino с демонстрацией федеративных запросов.
- Интеграция в дата-инженерию:
    - [06_integration_of_trino_into_de_python](06_integration_of_trino_into_de_python) — Интеграция Trino с Python.
    - [07_integration_of_trino_into_de_kafka](07_integration_of_trino_into_de_kafka) — Интеграция Trino с Kafka.
    - [08_integration_of_trino_into_de_apache_iceberg](08_integration_of_trino_into_de_apache_iceberg) — Интеграция
      Trino с
      Apache Iceberg.
    - [09_integration_of_trino_into_de_apache_airflow](09_integration_of_trino_into_de_apache_airflow) — Интеграция
      Trino с
      Apache Airflow.
    - [10_integration_of_trino_into_de_apache_superset](10_integration_of_trino_into_de_apache_superset) — Интеграция
      Trino
      с Apache Superset.