import logging

import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.trino.hooks.trino import TrinoHook

# Конфигурация DAG
OWNER = "i.korsakov"
DAG_ID = "simple_dag"

LONG_DESCRIPTION = """
# LONG DESCRIPTION

"""

SHORT_DESCRIPTION = "SHORT DESCRIPTION"

# Описание возможных ключей для default_args
# https://github.com/apache/airflow/blob/343d38af380afad2b202838317a47a7b1687f14f/airflow/example_dags/tutorial.py#L39
args = {
    "owner": OWNER,
    "start_date": pendulum.datetime(year=2025, month=1, day=1, tz="UTC"),
    "retries": 3,
    "retry_delay": pendulum.duration(hours=1),
}


def simple_task(**context) -> None:
    """
    Печатает контекст DAG.

    @param context: Контекст DAG.
    @return: Ничего не возвращает.
    """

    for context_key, context_key_value in context.items():
        logging.info(
            f"key_name – {context_key} | "
            f"value_name – {context_key_value} | "
            f"type_value_name – {type(context_key_value)}",
        )


def analyze_orders():
    # Инициализируем хук
    hook = TrinoHook(trino_conn_id="trino_default")

    # Вариант А: Получить сразу Pandas DataFrame
    # Хук сам создаст подключение и закроет его
    df = hook.get_pandas_df(sql="SELECT * FROM tpch.sf1.orders LIMIT 1000")

    print(f"Stats: {df.describe()}")

    # Вариант Б: Если нужно низкоуровневое соединение (DBAPI)
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM tpch.sf1.customer")
    result = cursor.fetchone()
    print(f"Count: {result}")


with DAG(
    dag_id=DAG_ID,
    schedule_interval="0 10 * * *",
    default_args=args,
    tags=["context"],
    description=SHORT_DESCRIPTION,
    concurrency=1,
    max_active_tasks=1,
    max_active_runs=1,
) as dag:
    dag.doc_md = LONG_DESCRIPTION

    start = EmptyOperator(
        task_id="start",
    )

    simple_task = PythonOperator(
        task_id="simple_task",
        python_callable=simple_task,
    )

    run_trino_sql_query = SQLExecuteQueryOperator(
        task_id="run_trino_query",
        conn_id="trino_default",
        sql="""
            CREATE TABLE IF NOT EXISTS memory.default.orders_summary AS
            SELECT orderdate, count(orderkey) as cnt
            FROM tpch.sf1.orders
            GROUP BY 1
        """,
    )

    run_trino_hook = PythonOperator(
        task_id="run_trino_hook",
        python_callable=analyze_orders,
    )

    end = EmptyOperator(
        task_id="end",
    )

    start >> simple_task >> run_trino_sql_query >> run_trino_hook >> end