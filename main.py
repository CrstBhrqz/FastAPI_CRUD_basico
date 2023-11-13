from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

# para implementar modelos o conocidos como esquemas 
from pydantic import BaseModel,Field
from typing import Optional


from routers.movie import movie_router
from routers.login import login_router

#-------------------------BD-------------------------------
from config.database import Session,engine,Base
from models.movie import Movie as MovieModel  #tabla
from fastapi.encoders import jsonable_encoder



#-------------------------middleware-------------------------------
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_handler import JWTBearer


app = FastAPI() # se crea la aplicacion y se instancia

#documnetacion
app.title = "mi aplicación con fastAPI" # para documentacion 
app.version = "0.0.1"
app.add_middleware(ErrorHandler)        # implementacion de errores middleware

#------------------------Rutas---------------------------------------
app.include_router(movie_router)
app.include_router(login_router)



#------------------------creacion de la tabla
Base.metadata.create_all(bind=engine)







#movies
movies=[
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Accións'    
    },
        {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
        {
        'id': 3,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    }  
]



# end Points
@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>hello world</h1>')
