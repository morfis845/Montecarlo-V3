from extract.leagues import LeagueExtractor

from transform.leagues import LeagueTransformer

from transform.seasons import SeasonTransformer

from loaders.duckdb_loader import DuckDBLoader


class DownloadLeaguesPipeline:

    def run(self):

        print("\nDownloading leagues...\n")

        response = LeagueExtractor().download()["response"]

        league_df = LeagueTransformer().transform(response)

        season_df = SeasonTransformer().transform(response)

        loader = DuckDBLoader()

        loader.insert_dataframe(

            league_df,

            "dim_league"

        )


        loader.insert_dataframe(

            season_df,

            "dim_season"

        )

        loader.close()

        print(f"Leagues: {len(league_df)}")
        print(f"Seasons: {len(season_df)}")

        print("\nDone.\n")