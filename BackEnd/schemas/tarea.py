
from pydantic import BaseModel

class Tarea(BaseModel):
    id_tarea: int
    id_user: int
    tarea: str
    descri: str
 
