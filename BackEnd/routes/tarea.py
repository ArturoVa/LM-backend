from fastapi import APIRouter, Response, status,HTTPException
from config.db import conn
from models.tarea import tareas
from schemas.tarea import Tarea
from config.db import conn
from starlette.responses import JSONResponse
from typing import List

tarea=APIRouter()

# Todos las tareas de un usuario
@tarea.get("/tasks/{id_user}", response_model=List[Tarea],tags=["Tareas"])
def get_tareas(id_user: str):
    query = tareas.select().where(tareas.c.id_user == id_user)
    result = conn.execute(query).fetchall()
    return result

# Crear una tarea -- tiene error 
@tarea.post("/tasks/{id_user}",response_model=Tarea,tags=["Tareas"])
def tarea_user(tarea: Tarea, id_user:str):
    new_tarea = {"id_user": id_user, "tarea": tarea.tarea , "descri":tarea.descri}
    result = conn.execute(tareas.insert().values(new_tarea))
    new_tarea_id = result.lastrowid
    conn.commit()
    new_tarea1 = conn.execute(tareas.select().where(tareas.c.id_tarea == new_tarea_id)).first()
    return new_tarea1 


# Tomar una tarea con un id especifico
@tarea.get("/tasks/{id_user}/{id_tarea}",response_model=Tarea,tags=["Tareas"])
def get_user(id_tarea:str , id_user:str):
    tarea = conn.execute(tareas.select().where( (tareas.c.id_user == id_user) & (tareas.c.id_tarea == id_tarea))).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Task not found")
    return tarea

#Actualizacion de tarea
@tarea.put("/tasks/{id_user}/{id_tarea}",response_model=Tarea,tags=["Tareas"])
def update_user(id_tarea:str, id_user:str ,tarea: Tarea):
    conn.execute(tareas.update().values(tarea =tarea.tarea , 
                                       descri=tarea.descri))
    return conn.execute(tareas.select().where( (tareas.c.id_user == id_user) & (tareas.c.id_tarea == id_tarea))).first()

#Eliminar tarea
@tarea.delete("/tasks/{id_user}/{id_tarea}",status_code=status.HTTP_204_NO_CONTENT,tags=["Tareas"])
def delete_user(id_tarea:str ,id_user:str):
    result = conn.execute(tareas.select().where((tareas.c.id_tarea == id_tarea) & (tareas.c.id_user == id_user))).first()
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    conn.execute(tareas.delete().where(tareas.c.id_tarea == id_tarea))
    return JSONResponse(content={"Tarea eliminada satisfactoriamente": "Task deleted successfully"}, status_code=200)

