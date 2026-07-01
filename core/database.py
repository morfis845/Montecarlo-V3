from pathlib import Path

import duckdb


DATABASE_PATH = Path("data/montecarlo_v3.duckdb")


class DatabaseManager:

    def __init__(self):

        self.connection = duckdb.connect(DATABASE_PATH)

    def execute(self, sql, parameters=None):

        if parameters is None:
            return self.connection.execute(sql)

        return self.connection.execute(sql, parameters)

    def executemany(self, sql, parameters):

        return self.connection.executemany(sql, parameters)

    def fetchone(self):

        return self.connection.fetchone()

    def fetchall(self):

        return self.connection.fetchall()

    def list_tables(self):

        return [

            row[0]

            for row in self.connection.execute(

                "SHOW TABLES"

            ).fetchall()

        ]

    def table_exists(self, table_name):

        return table_name in self.list_tables()

    def close(self):

        self.connection.close()