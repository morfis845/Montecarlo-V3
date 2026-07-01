from database.table_definition import *

TABLE = TableDefinition(

    name="dim_team",

    description="Stores football teams.",

    columns=[

        Column("team_id","INTEGER",False,True),

        Column("league_id","INTEGER",False),

        Column("season_id","INTEGER",False),

        Column("team_name","VARCHAR",False),

        Column("country","VARCHAR"),

        Column("founded","INTEGER"),

        Column("logo","VARCHAR"),

        Column("stadium_id","INTEGER"),

        Column("coach_id","INTEGER")

    ],

    foreign_keys=[

        ForeignKey("league_id","dim_league","league_id"),

        ForeignKey("season_id","dim_season","season_id"),

        ForeignKey("stadium_id","dim_stadium","stadium_id"),

        ForeignKey("coach_id","dim_coach","coach_id")

    ],

    indexes=[

        Index("idx_team_name",["team_name"]),

        Index("idx_team_league",["league_id"])

    ]

)