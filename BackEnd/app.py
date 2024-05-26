from fastapi import FastAPI
from routes.user import user
from routes.tarea import tarea
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Pia de lenguajes modernos",
    description="Se tiene 2 grupos, las tareas y los usuarios, cada uno tiene gets, post, deletes and puts"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user)
app.include_router(tarea)