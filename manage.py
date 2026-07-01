import argparse

from core.database import DatabaseManager

from database.create_database import DatabaseBuilder

from database.validator import DatabaseValidator


parser = argparse.ArgumentParser()

parser.add_argument("command")

args = parser.parse_args()


builder = DatabaseBuilder()


if args.command == "create-db":

    builder.create_tables()

    DatabaseValidator(

        builder.connection

    ).validate()

    print("\nDatabase created successfully.")


elif args.command == "show-tables":

    db = DatabaseManager()

    print()

    for table in db.list_tables():

        print(f"✔ {table}")

    db.close()


elif args.command == "validate-db":

    DatabaseValidator(

        builder.connection

    ).validate()

    print("\nDatabase validated successfully.")


elif args.command == "drop-db":

    builder.drop_database()

    print("\nDatabase deleted.")


elif args.command == "rebuild-db":

    builder.rebuild()

    DatabaseValidator(

        builder.connection

    ).validate()

    print("\nDatabase rebuilt successfully.")