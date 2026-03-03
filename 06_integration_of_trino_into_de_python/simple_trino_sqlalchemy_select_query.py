from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("trino://admin@localhost:8080/")

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
