from database.table_definition import *

TABLE = TableDefinition(

    name="dim_player",

    description="Stores football players.",

    columns=[

        Column("player_id","INTEGER",False,True),

        Column("team_id","INTEGER",False),

        Column("player_name","VARCHAR",False),

        Column("firstname","VARCHAR"),

        Column("lastname","VARCHAR"),

        Column("birth_date","DATE"),

        Column("nationality","VARCHAR"),

        Column("height","INTEGER"),

        Column("weight","INTEGER"),

        Column("position","VARCHAR"),

        Column("photo","VARCHAR")

    ],

    foreign_keys=[

        ForeignKey("team_id","dim_team","team_id")

    ],

    indexes=[

        Index("idx_player_team",["team_id"]),

        Index("idx_player_name",["player_name"])

    ]

)