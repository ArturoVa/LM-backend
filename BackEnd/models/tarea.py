from sqlalchemy import  Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine

# Modelo de la tabla Tareas
tareas = Table( "tareas", meta,
               #Elementos
              Column("id_tarea",Integer,primary_key=True, autoincrement=True), 
              Column("id_user",Integer,ForeignKey("usuarios.id_user")), 
              Column("tarea", String(255)),
              Column("descri", String(255))
)

#Comando para crear la tabla, no funca, error en la foreing key
meta.create_all(engine)

