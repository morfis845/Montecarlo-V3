import duckdb

connection = duckdb.connect("data/montecarlo_v3.duckdb")

tables = connection.execute("SHOW TABLES").fetchall()

print("\nTables\n")

for table in tables:
    print(f"✔ {table[0]}")

connection.close()