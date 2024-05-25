from fastapi import FastAPI
from routes.user import user
from routes.tarea import tarea


app = FastAPI(
    title="Pia de lenguajes modernos",
    description="Se tiene 2 grupos, las tareas y los usuarios, cada uno tiene gets,post,deletes and puts"
)

app.include_router(user)
app.include_router(tarea)

