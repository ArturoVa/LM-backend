from fastapi import APIRouter, HTTPException
from config.db import conn
from models.user import users
from schemas.user import User
from starlette.responses import JSONResponse
from cryptography.fernet import Fernet
from typing import List
from models.tarea import tareas
#Para encryptar la password
key=Fernet.generate_key()
cryptar=Fernet(key)
user=APIRouter()

# Todos los usuarios
@user.get("/users",response_model=List[User],tags=["users"])
async def get_users():
    return conn.execute(users.select()).fetchall()

# Crear usuario
@user.post("/users",response_model=User,tags=["users"])
async def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"]= cryptar.encrypt(user.password.encode("utf-8"))
    result =conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id_user == result.lastrowid)).first()

# Tomar un usuarion con un id
@user.get("/users/{id_user}",response_model=User,tags=["users"])
async def get_user(id_user:str):
    result = conn.execute(users.select().where(users.c.id_user == id_user)).first()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result

#Actualizacion de usuario 
@user.put("/users/{id_user}",response_model=User,tags=["users"])
async def update_user(id_user:str , user: User):
    conn.execute(users.update().values(name = user.name , 
                                       email= user.email , 
                                       password =cryptar.encrypt(user.password.encode("utf-8"))
                ).where(users.c.id_user == id_user))
    return conn.execute(users.select().where(users.c.id_user == id_user)).first()


#Eliminar Usuario
@user.delete("/users/{id_user}",tags=["users"])
async def delete_user(id_user:str):
    result2 = conn.execute(tareas.select().where(tareas.c.id_user == id_user)).fetchall()
    if not result2:
        raise HTTPException(status_code=404, detail="Task not found")
    conn.execute(tareas.delete().where(tareas.c.id_user == id_user))
    result=conn.execute(users.delete().where(users.c.id_user == id_user))
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    conn.execute(users.delete().where(users.c.id_user == id_user))
    return JSONResponse(content={"Usuario eliminado exitosamente": "User deleted successfully"}, status_code=200)
