from database.table_definition import *

TABLE = TableDefinition(

    name="fact_player_match",

    description="Stores player statistics for each fixture.",

    columns=[

        Column("fixture_id", "INTEGER", nullable=False),

        Column("team_id", "INTEGER", nullable=False),

        Column("player_id", "INTEGER", nullable=False),

        Column("minutes", "INTEGER"),

        Column("shirt_number", "INTEGER"),

        Column("position", "VARCHAR"),

        Column("rating", "DOUBLE"),

        Column("captain", "BOOLEAN"),

        Column("substitute", "BOOLEAN"),

        Column("offsides", "INTEGER"),

        Column("shots_total", "INTEGER"),

        Column("shots_on_target", "INTEGER"),

        Column("goals", "INTEGER"),

        Column("assists", "INTEGER"),

        Column("goals_conceded", "INTEGER"),

        Column("goalkeeper_saves", "INTEGER"),

        Column("passes_total", "INTEGER"),

        Column("passes_key", "INTEGER"),

        Column("passes_accuracy", "INTEGER"),

        Column("tackles", "INTEGER"),

        Column("blocks", "INTEGER"),

        Column("interceptions", "INTEGER"),

        Column("duels_total", "INTEGER"),

        Column("duels_won", "INTEGER"),

        Column("dribbles_attempts", "INTEGER"),

        Column("dribbles_success", "INTEGER"),

        Column("dribbled_past", "INTEGER"),

        Column("fouls_drawn", "INTEGER"),

        Column("fouls_committed", "INTEGER"),

        Column("yellow_cards", "INTEGER"),

        Column("red_cards", "INTEGER"),

        Column("penalties_won", "INTEGER"),

        Column("penalties_committed", "INTEGER"),

        Column("penalties_scored", "INTEGER"),

        Column("penalties_missed", "INTEGER"),

        Column("penalties_saved", "INTEGER"),

    ],

    foreign_keys=[

        ForeignKey(
            "fixture_id",
            "fact_fixture",
            "fixture_id"
        ),

        ForeignKey(
            "team_id",
            "dim_team",
            "team_id"
        ),

        ForeignKey(
            "player_id",
            "dim_player",
            "player_id"
        )

    ],

    indexes=[

        Index(
            "idx_player_fixture",
            ["fixture_id"]
        ),

        Index(
            "idx_player_team",
            ["team_id"]
        ),

        Index(
            "idx_player",
            ["player_id"]
        )

    ]

)