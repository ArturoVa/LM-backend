
from pydantic import BaseModel



class User(BaseModel):
    id_user: int
    name: str
    email: str
    password:str





