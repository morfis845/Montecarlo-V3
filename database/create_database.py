import duckdb

from pathlib import Path

from database.builder import (
    build_create_table,
    build_indexes
)

from database.registry import TABLES

DATABASE_PATH = Path(
    "data/montecarlo_v3.duckdb"
)


class DatabaseBuilder:

    def __init__(self):

        DATABASE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.connection = duckdb.connect(
            DATABASE_PATH
        )

    def create_tables(self):

        for table in TABLES:

            self.connection.execute(

                build_create_table(table)

            )

            for index in build_indexes(table):

                self.connection.execute(index)

    def close(self):

        self.connection.close()

    def drop_database(self):

        self.close()

        if DATABASE_PATH.exists():

            DATABASE_PATH.unlink()


    def rebuild(self):

        self.drop_database()

        self.__init__()

        self.create_tables()