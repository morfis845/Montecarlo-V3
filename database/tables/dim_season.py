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
            name="season_id",
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
            name="season",
            data_type="INTEGER",
            nullable=False
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