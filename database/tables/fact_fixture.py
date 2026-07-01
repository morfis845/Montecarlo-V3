from database.table_definition import *

TABLE = TableDefinition(

    name="fact_fixture",

    description="Stores football fixtures.",

    columns=[

        Column(
            "fixture_id",
            "INTEGER",
            primary_key=True,
            nullable=False
        ),

        Column(
            "league_id",
            "INTEGER",
            nullable=False
        ),

        Column(
            "season",
            "INTEGER",
            nullable=False
        ),

        Column(
            "date",
            "TIMESTAMP",
            nullable=False
        ),

        Column(
            "timestamp",
            "BIGINT",
            nullable=False
        ),

        Column(
            "timezone",
            "VARCHAR",
            nullable=False
        ),

        Column(
            "round",
            "VARCHAR",
            nullable=False
        ),

    ],

    foreign_keys=[

        ForeignKey(
            "league_id",
            "dim_league",
            "league_id"
        )

    ],

    indexes=[

        Index(
            "idx_fixture_date",
            ["date"]
        ),

        Index(
            "idx_fixture_league",
            ["league_id"]
        )

    ]

)