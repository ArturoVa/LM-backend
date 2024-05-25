from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine



# Modelo de la tabla usuarios
users = Table( "usuarios", meta,
                Column("id_user",Integer,primary_key=True,nullable=False),
                Column("name",String(255)), 
                Column("email", String(255)),
                Column("password", String(255)),
    
)

#Comando para crear la tabla, no funca, error en la foreing key
meta.create_all(engine)

