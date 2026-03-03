import pandas as pd
from random import randint
import uuid
from trino.dbapi import connect

# 1. Создаем тестовый датафрейм (ваш код)
dict_ = {
    'id': [randint(a=10, b=100) for _ in range(10)],
    'value': [randint(a=100, b=1000) for _ in range(10)],
    'str': [str(uuid.uuid4()) for _ in range(10)]
}
df = pd.DataFrame.from_dict(dict_)

# 2. Подключение к Trino
conn = connect(
    host="localhost",
    port=8080,
    user="admin",
)
cur = conn.cursor()

# 3. Создаем таблицу
try:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS memory."default".foo
        (
            id bigint,
            value bigint,
            str varchar
        )
    """)
    print("Таблица готова.")
except Exception as e:
    print(f"Ошибка при создании таблицы: {e}")

insert_sql = 'INSERT INTO memory."default".foo (id, value, str) VALUES (?, ?, ?)'

data_to_insert = list(df.itertuples(index=False, name=None))

cur.executemany(insert_sql, data_to_insert)
conn.commit()

cur.close()
conn.close()
