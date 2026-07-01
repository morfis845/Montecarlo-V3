from database.table_definition import *

TABLE = TableDefinition(

    name="dim_stadium",

    description="Stores stadiums.",

    columns=[

        Column("stadium_id","INTEGER",False,True),

        Column("stadium_name","VARCHAR",False),

        Column("city","VARCHAR"),

        Column("country","VARCHAR"),

        Column("capacity","INTEGER")

    ],

    indexes=[

        Index("idx_stadium_name",["stadium_name"])

    ]

)