from database.table_definition import *

TABLE = TableDefinition(

    name="dim_team",

    description="Stores football teams.",

    columns=[

        Column("team_id", "INTEGER", primary_key=True, nullable=False),

        Column("team_name", "VARCHAR", nullable=False),

        Column("team_code", "VARCHAR"),

        Column("country", "VARCHAR"),

        Column("founded", "INTEGER"),

        Column("national", "BOOLEAN"),

        Column("logo", "VARCHAR"),

    ],

    foreign_keys=[],

    indexes=[

    ]

)