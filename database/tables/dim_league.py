from database.table_definition import (
    Column,
    Index,
    TableDefinition
)

TABLE = TableDefinition(

    name="dim_league",

    description="Stores football leagues.",

    columns=[

        Column(
            name="league_id",
            data_type="INTEGER",
            primary_key=True,
            nullable=False
        ),

        Column(
            name="league_name",
            data_type="VARCHAR",
            nullable=False
        ),

        Column(
            name="country",
            data_type="VARCHAR",
            nullable=False
        ),

        Column(
            name="type",
            data_type="VARCHAR",
            nullable=False
        ),

        Column(
            name="logo",
            data_type="VARCHAR"
        ),
        Column(
            name="country_code",
            data_type="VARCHAR"
        ),

        Column(
            name="country_flag",
            data_type="VARCHAR"
        ),

    ],

    indexes=[

        Index(
            name="idx_dim_league_country",
            columns=["country"]
        )

    ]

)