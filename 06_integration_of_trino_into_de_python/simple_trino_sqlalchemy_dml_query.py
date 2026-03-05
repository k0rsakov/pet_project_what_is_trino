import uuid
from random import randint

import pandas as pd
from sqlalchemy import create_engine

# 1. Создаем тестовый датафрейм
dict_ = {
    'id': [randint(a=10, b=100) for _ in range(10)],
    'value': [randint(a=100, b=1000) for _ in range(10)],
    'str': [str(uuid.uuid4()) for _ in range(10)]
}

df = pd.DataFrame.from_dict(dict_)
# 2. Создаём движок для работы с Trino
engine = create_engine('trino://admin@localhost:8080/memory/default')

# Вставка одним вызовом
# if_exists='append' добавит данные, 'replace' пересоздаст таблицу
df.to_sql(
    name='foo',
    con=engine,
    if_exists='append',
    index=False,
    method='multi',
)
