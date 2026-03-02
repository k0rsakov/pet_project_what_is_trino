from sqlalchemy import create_engine
import pandas as pd

conn_str = "trino://admin@localhost:8080/"

engine = create_engine(conn_str)

df = pd.read_sql_query(
    sql="""
    SELECT
      orderdate,
      count(orderKey) AS cnt_orders,
      sum(totalprice) AS sum_orders
    FROM
      tpch.sf1.orders
    WHERE
      1=1
    GROUP BY
      1
    """,
    con=engine,
)

print(df)
