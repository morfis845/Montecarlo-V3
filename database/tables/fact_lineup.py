from database.table_definition import (
    Column,
    ForeignKey,
    Index,
    TableDefinition
)

TABLE = TableDefinition(

    name="fact_lineup",

    description="Stores match lineups.",

    columns=[

        Column("fixture_id","INTEGER",False,True),

        Column("player_id","INTEGER",False,True),

        Column("team_id","INTEGER",False),

        Column("is_starter","BOOLEAN",False),

        Column("shirt_number","INTEGER"),

        Column("formation_position","VARCHAR"),

        Column("created_at","TIMESTAMP",False,default="CURRENT_TIMESTAMP")

    ],

    foreign_keys=[

        ForeignKey("fixture_id","fact_fixture","fixture_id"),

        ForeignKey("player_id","dim_player","player_id"),

        ForeignKey("team_id","dim_team","team_id")

    ],

    indexes=[

        Index("idx_lineup_fixture",["fixture_id"]),

        Index("idx_lineup_team",["team_id"])

    ]

)