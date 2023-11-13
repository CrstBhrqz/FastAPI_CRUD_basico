from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Path, Query
from typing import List

#-------------esquemas------------------------------
from schemas.movie import Movie 


#-------------------------BD-------------------------------
from config.database import Session
from models.movie import Movie as MovieModel  #tabla
from fastapi.encoders import jsonable_encoder


from services.movie import MovieService





movie_router = APIRouter()          #Nombre de la ruta a importar


#---------------------------------------------------------------------------CRUD---------------------------------------

#----------------CREADE--------------------------
@movie_router.post('/movies', tags=['movies'],response_model=dict,status_code=201)
def create_movie(movie:Movie):
    db = Session()                           # conectarme a la base de datos
    # new_movie =MovieModel(**movie.dict())    #pasa los parametros
    # db.add(new_movie)                        #ingresa el modelos 
    # db.commit()                              #actualiza los cambios
    resul =  MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201,content={"mansaje":"Se registro la pelicula"})



#----------------READ--------------------------
#@app.get('/movies',tags=['movies'],status_code=200, dependencies=[Depends(JWTBearer())])#implementacion de la clase para pedir token y poder mostar informacion
@movie_router.get('/movies',tags=['movies'],status_code=200)#sin token 
def get_movies():
    db = Session()                                  # conectarme a la base de datos
    # resul = db.query(MovieModel).all()              # consulta de la tabla      NORMAL
    resul =  MovieService(db).get_movies()          # consulta de la tabla      SERVICIO
    return JSONResponse(status_code=200,content=jsonable_encoder(resul))


@movie_router.get('/movies/{id}',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movie(id:int=Path(ge=1, le=2000)):
    db = Session()                                                      # conectarme a la base de datos
    # resul = db.query(MovieModel).filter(MovieModel.id == id ).first() # consulta por id y entrega el primero      NORMAL
    resul = MovieService(db).get_movie(id)                              # consulta por id y entrega el primero      SERVICIE
    if not resul:
        return JSONResponse(status_code=404,content=[])
    return JSONResponse(status_code=200,content=jsonable_encoder(resul))


@movie_router.get('/movies/',tags=['movies'],response_model=List[Movie])
def get_movies_by_category(category:str = Query(min_length=5,max_length=15)) ->List[Movie]:
    db = Session()                                                                      # conectarme a la base de datos
    # resul = db.query(MovieModel).filter(MovieModel.category == category).all()        #hace la consulta por categoria  Normal
    resul = MovieService(db).get_category(category)    #hace la consulta por categoria  #hace la consulta por categoria  SERVICIE 
    # data= [item for item in movies if item['category']== category]                  
    return JSONResponse(content=jsonable_encoder(resul))


#----------------UPDATE--------------------------

@movie_router.put('/movies/{id}', tags=['movies'],response_model=dict,status_code=200)
def update_movie(id:int, movie:Movie)->dict:
    db = Session()                                                                  # conectarme a la base de datos
    resul = MovieService(db).get_movie(id)              #hace la consulta por categoria verfica la existencia  
    if not resul:
        return JSONResponse(status_code=404,content={"mansaje":"Error de actualizacion"})  #valida  
    MovieService(db).update_movie(id,movie)  
    return JSONResponse(status_code=200,content={"mansaje":"actualizada Pelicula"})

#----------------DELETE--------------------------
@movie_router.delete('/movies', tags=['movies'],response_model=dict,status_code=200)
def delete_movie(id:int) -> dict:
    db = Session()                                                                  # conectarme a la base de datos
    # resul = db.query(MovieModel).filter(MovieModel.id == id ).first()               #hace la consulta por categoria verfica la existencia  
    resul = MovieService(db).get_movie(id)                    #hace la consulta por categoria verfica la existencia  
    if not resul:
        return JSONResponse(status_code=404,content={"mansaje":"Error de actualizacion"})
    MovieService(db).delte_movie(id)
    return JSONResponse(status_code=200,content={"mansaje":"Eliminada la Pelicula"})

