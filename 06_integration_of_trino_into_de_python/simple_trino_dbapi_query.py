from trino.dbapi import connect

conn = connect(
    host="localhost",
    port=8080,
    user="admin",
)
cur = conn.cursor()
cur.execute("SELECT * FROM system.runtime.nodes")
rows = cur.fetchall()

print(rows)