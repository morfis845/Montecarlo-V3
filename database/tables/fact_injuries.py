from database.table_definition import (
    Column,
    ForeignKey,
    Index,
    TableDefinition
)

TABLE = TableDefinition(

    name="fact_injuries",

    description="Stores player injuries.",

    columns=[

        Column("injury_id","INTEGER",False,True),

        Column("player_id","INTEGER",False),

        Column("team_id","INTEGER",False),

        Column("fixture_id","INTEGER"),

        Column("injury_type","VARCHAR"),

        Column("status","VARCHAR"),

        Column("expected_return","DATE"),

        Column("created_at","TIMESTAMP",False,default="CURRENT_TIMESTAMP")

    ],

    foreign_keys=[

        ForeignKey("player_id","dim_player","player_id"),

        ForeignKey("team_id","dim_team","team_id"),

        ForeignKey("fixture_id","fact_fixture","fixture_id")

    ],

    indexes=[

        Index("idx_injury_player",["player_id"]),

        Index("idx_injury_team",["team_id"])

    ]

)