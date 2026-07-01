from core.database import DatabaseManager


class DuckDBLoader:

    def __init__(self):

        self.db = DatabaseManager()

    def insert_dataframe(self, dataframe, table_name):

        if dataframe.empty:

            print(f"No records to insert into {table_name}.")

            return

        self.db.connection.register(
            "temp_df",
            dataframe
        )

        columns = list(dataframe.columns)

        column_list = ", ".join(columns)

        sql = f"""
        INSERT INTO {table_name}
        ({column_list})
        SELECT {column_list}
        FROM temp_df
        """

        self.db.execute(sql)

        self.db.connection.unregister(
            "temp_df"
        )

        print(

            f"Inserted {len(dataframe)} rows into {table_name}."

        )

    def close(self):

        self.db.close()