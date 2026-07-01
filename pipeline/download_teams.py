from extract.teams import TeamExtractor

from transform.teams import TeamTransformer
from transform.stadiums import StadiumTransformer

from loaders.duckdb_loader import DuckDBLoader


class DownloadTeamsPipeline:

    def run(self, league_id, season):

        print("\nDownloading teams...\n")

        response = TeamExtractor().download(

            league_id,
            season

        )["response"]

        team_df = TeamTransformer().transform(response)

        stadium_df = StadiumTransformer().transform(response)

        print(f"Teams: {len(team_df)}")
        print(f"Stadiums: {len(stadium_df)}")

        loader = DuckDBLoader()

        loader.insert_dataframe(

            team_df,

            "dim_team"

        )

        loader.insert_dataframe(

            stadium_df,

            "dim_stadium"

        )

        loader.close()

        print("\nDone.\n")