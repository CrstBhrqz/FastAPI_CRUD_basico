# para implementar modelos o conocidos como esquemas 
from pydantic import BaseModel,Field
from typing import  Optional, List

class Movie(BaseModel):
    id: Optional[int]= None # inidica que el campo puede ser opcional
    title : str = Field(default="mi pelicula", min_length=5, max_length=15)
    overview:str = Field(default="Descripcion de la pelicula", min_length=15, max_length=150)
    year:str = Field(default='2022', min_length=1, max_length=5)
    rating:float = Field(ge=1, le=2022)
    category:str =Field(default="accion", min_length=5, max_length=15)
