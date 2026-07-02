from database.table_definition import *

TABLE = TableDefinition(

    name="dim_player",

    description="Stores football players.",

    columns=[

        Column("player_id", "INTEGER", primary_key=True, nullable=False),

        Column("player_name", "VARCHAR", nullable=False),

        Column("firstname", "VARCHAR"),

        Column("lastname", "VARCHAR"),

        Column("birth_date", "DATE"),

        Column("nationality", "VARCHAR"),

        Column("height", "INTEGER"),

        Column("weight", "INTEGER"),

        Column("position", "VARCHAR"),

        Column("photo", "VARCHAR")

    ],

    indexes=[

        Index("idx_player_name", ["player_name"])

    ]

)