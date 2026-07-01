from database.table_definition import (
    Column,
    ForeignKey,
    Index,
    TableDefinition
)

TABLE = TableDefinition(

    name="fact_odds",

    description="Stores bookmaker odds.",

    columns=[

        Column("odd_id","INTEGER",False,True),

        Column("fixture_id","INTEGER",False),

        Column("bookmaker","VARCHAR",False),

        Column("market","VARCHAR",False),

        Column("selection","VARCHAR",False),

        Column("odd","DOUBLE",False),

        Column("created_at","TIMESTAMP",False,default="CURRENT_TIMESTAMP")

    ],

    foreign_keys=[

        ForeignKey("fixture_id","fact_fixture","fixture_id")

    ],

    indexes=[

        Index("idx_odds_fixture",["fixture_id"]),

        Index("idx_odds_market",["market"])

    ]

)