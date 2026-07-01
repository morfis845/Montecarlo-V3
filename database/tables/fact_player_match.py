from database.table_definition import (
    Column,
    ForeignKey,
    Index,
    TableDefinition
)

TABLE = TableDefinition(

    name="fact_player_match",

    description="Stores player statistics for each fixture.",

    columns=[

        Column("fixture_id","INTEGER",False,True),

        Column("player_id","INTEGER",False,True),

        Column("team_id","INTEGER",False),

        Column("minutes","INTEGER"),

        Column("position","VARCHAR"),

        Column("rating","DOUBLE"),

        Column("goals","INTEGER"),

        Column("assists","INTEGER"),

        Column("shots","INTEGER"),

        Column("shots_on_target","INTEGER"),

        Column("passes","INTEGER"),

        Column("key_passes","INTEGER"),

        Column("tackles","INTEGER"),

        Column("interceptions","INTEGER"),

        Column("yellow_cards","INTEGER"),

        Column("red_cards","INTEGER"),

        Column("created_at","TIMESTAMP",False,default="CURRENT_TIMESTAMP")

    ],

    foreign_keys=[

        ForeignKey("fixture_id","fact_fixture","fixture_id"),

        ForeignKey("player_id","dim_player","player_id"),

        ForeignKey("team_id","dim_team","team_id")

    ],

    indexes=[

        Index("idx_player_fixture",["fixture_id"]),

        Index("idx_player",["player_id"])

    ]

)