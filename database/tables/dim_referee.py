from database.table_definition import *

TABLE = TableDefinition(

    name="dim_referee",

    description="Stores referees.",

    columns=[

        Column("referee_id","INTEGER",False,True),

        Column("referee_name","VARCHAR",False),

        Column("country","VARCHAR")

    ]

)