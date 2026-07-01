from database.table_definition import (
    Column,
    ForeignKey,
    Index,
    TableDefinition
)

TABLE = TableDefinition(

    name="fact_team_match",

    description="Stores team statistics for each fixture.",

    columns=[

        Column("fixture_id","INTEGER",False,True),

        Column("team_id","INTEGER",False,True),

        Column("is_home","BOOLEAN",False),

        Column("goals","INTEGER"),

        Column("halftime_goals","INTEGER"),

        Column("shots","INTEGER"),

        Column("shots_on_target","INTEGER"),

        Column("corners","INTEGER"),

        Column("offsides","INTEGER"),

        Column("fouls","INTEGER"),

        Column("yellow_cards","INTEGER"),

        Column("red_cards","INTEGER"),

        Column("possession","DOUBLE"),

        Column("formation","VARCHAR"),

        Column("created_at","TIMESTAMP",False,default="CURRENT_TIMESTAMP")

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
        )

    ],

    indexes=[

        Index(
            "idx_team_fixture",
            ["fixture_id"]
        ),

        Index(
            "idx_team",
            ["team_id"]
        )

    ]

)