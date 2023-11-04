from fastapi import Depends, FastAPI,Body, HTTPException, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse

# para implementar modelos o conocidos como esquemas 
from pydantic import BaseModel,Field
from typing import Any, Coroutine, Optional, List

from starlette.requests import Request

from jwt_manager import create_token,validate_token
from fastapi.security import HTTPBearer



app = FastAPI() # se crea la aplicacion y se instancia

#documnetacion
app.title = "mi aplicación con fastAPI" # para documentacion 
app.version = "0.0.1"

# modelo de movies 
class Movie(BaseModel):
    id: Optional[int]= None # inidica que el campo puede ser opcional
    title : str = Field(default="mi pelicula", min_length=5, max_length=15)
    overview:str = Field(default="Descripcion de la pelicula", min_length=15, max_length=150)
    year:str = Field(default='2022', min_length=1, max_length=5)
    rating:float = Field(ge=1, le=2022)
    category:str =Field(default="accion", min_length=5, max_length=15)

    # class Config:
    #     schema_estra = {
    #         "example":{
    #             "id":1,
    #             'title': 'Avatar',
    #             'overview': "Descripcion de la pelicula",
    #             'year': '2022',
    #             'rating': 9.8,
    #             'category': 'Acción'   
    #         }
    #     }


class User(BaseModel):
    email:str
    password:str

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403,detail="credenciales son ivalidas")






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


@app.get('/movies',tags=['movies'],status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies():
    return JSONResponse(status_code=200,content=movies)


@app.get('/movies/{id}',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movies(id:int=Path(ge=1, le=2000)):
    for item in movies:
        print(item)
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404,content=[])


@app.get('/movies/',tags=['movies'],response_model=List[Movie])
def get_movies_by_category(category:str = Query(min_length=5,max_length=15)) ->List[Movie]:
    data= [item for item in movies if item['category']== category]
    return JSONResponse(content=data)


@app.post('/movies', tags=['movies'],response_model=dict,status_code=201)
def create_movie(movie:Movie):
    movies.append(movie.dict())
    return JSONResponse(status_code=201,content={"mansaje":"exito"})


@app.delete('/movies', tags=['movies'],response_model=dict,status_code=200)
def delete_movie(id:int) -> dict:
    print(movies)
    for item in movies:
        if item['id']==id:
            movies.remove(item)
            return JSONResponse(status_code=200,content={"mansaje":"Eliminada la Pelicula"})

@app.put('/movies/{id}', tags=['movies'],response_model=dict,status_code=200)
def update_movie(id:int, movie:Movie)->dict:
    for item in movies:
        if item['id']==id:
            item['title']= movie.title
            item['overview']= movie.overview
            item['year']= movie.year
            item['rating']= movie.rating
            item['category']= movie.category   
    return JSONResponse(status_code=200,content={"mansaje":"actualizada Pelicula"})



@app.post('/login', tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password== "123456":
        token:str=create_token(user.dict())
        return JSONResponse(status_code=200,content=token)
    return JSONResponse(status_code=404,content={"mansaje":"validacion incorrecta"})

@app.post('/validar', tags=['auth'])
def validar(token:str):
    return validate_token(token)