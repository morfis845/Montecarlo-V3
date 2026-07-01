from database.table_definition import *

TABLE = TableDefinition(

    name="dim_stadium",

    description="Stores stadiums.",

    columns=[

        Column(
            name="stadium_id",
            data_type="INTEGER",
            primary_key=True,
            nullable=False
        ),

        Column(
            name="stadium_name",
            data_type="VARCHAR",
            nullable=False
        ),

        Column(
            name="address",
            data_type="VARCHAR"
        ),

        Column(
            name="city",
            data_type="VARCHAR"
        ),

        Column(
            name="capacity",
            data_type="INTEGER"
        ),

        Column(
            name="surface",
            data_type="VARCHAR"
        ),

        Column(
            name="image",
            data_type="VARCHAR"
        ),

    ],

    indexes=[

        Index("idx_stadium_name",["stadium_name"])

    ]

)