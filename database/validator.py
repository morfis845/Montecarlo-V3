from database.registry import TABLES


class DatabaseValidator:

    def __init__(self, connection):

        self.connection = connection

    def validate(self):

        existing = {

            row[0]

            for row in self.connection.execute(

                "SHOW TABLES"

            ).fetchall()

        }

        expected = {

            table.name

            for table in TABLES

        }

        missing = expected - existing

        extra = existing - expected

        if missing:

            raise RuntimeError(

                f"Missing tables: {sorted(missing)}"

            )

        if extra:

            print(

                f"Warning: extra tables detected: {sorted(extra)}"

            )

        return True