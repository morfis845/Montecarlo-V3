import argparse

from core.database import DatabaseManager

from database.create_database import DatabaseBuilder

from database.validator import DatabaseValidator


parser = argparse.ArgumentParser()

parser.add_argument("command")

parser.add_argument("--league", type=int)

parser.add_argument("--season", type=int)

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

elif args.command == "download-leagues":

    from pipeline.download_leagues import DownloadLeaguesPipeline

    DownloadLeaguesPipeline().run()

elif args.command == "count":

    db = DatabaseManager()

    table = input("Table: ")

    rows = db.execute(

        f"SELECT COUNT(*) FROM {table}"

    ).fetchone()[0]

    print(

        f"\n{table}: {rows} rows"

    )

    db.close()

elif args.command == "preview":

    import pandas as pd

    db = DatabaseManager()

    table = input("Table: ")

    df = db.execute(

        f"SELECT * FROM {table} LIMIT 10"

    ).fetchdf()

    print()

    print(df)

    db.close()
    
elif args.command == "download-teams":

    from pipeline.download_teams import DownloadTeamsPipeline

    DownloadTeamsPipeline().run(

        league_id=args.league,

        season=args.season

    )