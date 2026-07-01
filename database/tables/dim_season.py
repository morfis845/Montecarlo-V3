from database.table_definition import (
    Column,
    ForeignKey,
    Index,
    TableDefinition
)

TABLE = TableDefinition(

    name="dim_season",

    description="Stores league seasons.",

    columns=[

        Column(
            name="league_id",
            data_type="INTEGER",
            nullable=False,
            primary_key=True
        ),

        Column(
            name="season",
            data_type="INTEGER",
            nullable=False,
            primary_key=True
        ),

        Column(
            name="start_date",
            data_type="DATE"
        ),

        Column(
            name="end_date",
            data_type="DATE"
        ),

        Column(
            name="current",
            data_type="BOOLEAN",
            nullable=False,
            default="FALSE"
        ),

        # ===== Coverage =====

        Column("coverage_events", "BOOLEAN"),

        Column("coverage_lineups", "BOOLEAN"),

        Column("coverage_fixture_statistics", "BOOLEAN"),

        Column("coverage_player_statistics", "BOOLEAN"),

        Column("coverage_standings", "BOOLEAN"),

        Column("coverage_players", "BOOLEAN"),

        Column("coverage_top_scorers", "BOOLEAN"),

        Column("coverage_top_assists", "BOOLEAN"),

        Column("coverage_top_cards", "BOOLEAN"),

        Column("coverage_injuries", "BOOLEAN"),

        Column("coverage_predictions", "BOOLEAN"),

        Column("coverage_odds", "BOOLEAN"),

        # ===== ETL =====

        Column(
            name="api_last_update",
            data_type="TIMESTAMP",
            nullable=False,
            default="CURRENT_TIMESTAMP"
        )

    ],

    foreign_keys=[

        ForeignKey(
            column="league_id",
            reference_table="dim_league",
            reference_column="league_id"
        )

    ],

    indexes=[

        Index(
            name="idx_season_league",
            columns=["league_id"]
        )

    ]

)