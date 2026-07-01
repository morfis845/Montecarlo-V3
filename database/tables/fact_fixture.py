from database.table_definition import (
    Column,
    ForeignKey,
    Index,
    TableDefinition
)

TABLE = TableDefinition(

    name="fact_fixture",

    description="Stores football fixtures.",

    columns=[

        Column(
            name="fixture_id",
            data_type="INTEGER",
            primary_key=True,
            nullable=False
        ),

        Column(
            name="league_id",
            data_type="INTEGER",
            nullable=False
        ),

        Column(
            name="season_id",
            data_type="INTEGER",
            nullable=False
        ),

        Column(
            name="home_team_id",
            data_type="INTEGER",
            nullable=False
        ),

        Column(
            name="away_team_id",
            data_type="INTEGER",
            nullable=False
        ),

        Column(
            name="stadium_id",
            data_type="INTEGER"
        ),

        Column(
            name="referee_id",
            data_type="INTEGER"
        ),

        Column(
            name="fixture_date",
            data_type="TIMESTAMP",
            nullable=False
        ),

        Column(
            name="round",
            data_type="VARCHAR"
        ),

        Column(
            name="status",
            data_type="VARCHAR"
        ),

        Column(
            name="elapsed",
            data_type="INTEGER"
        ),

        Column(
            name="created_at",
            data_type="TIMESTAMP",
            nullable=False,
            default="CURRENT_TIMESTAMP"
        ),
        Column(
            name="season",
            data_type="INTEGER",
            nullable=False
        ),

        

    ],

    foreign_keys=[

        ForeignKey("league_id","dim_league","league_id"),
        
        ForeignKey("home_team_id","dim_team","team_id"),

        ForeignKey("away_team_id","dim_team","team_id"),

        ForeignKey("stadium_id","dim_stadium","stadium_id"),

        ForeignKey("referee_id","dim_referee","referee_id")

    ],

    indexes=[

        Index(
            "idx_fixture_date",
            ["fixture_date"]
        ),

        Index(
            "idx_fixture_league",
            ["league_id"]
        ),

        Index(
            "idx_fixture_season",
            ["season_id"]
        )

    ]

)