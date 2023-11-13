from fastapi import APIRouter
from fastapi.responses import JSONResponse


from schemas.user import User


#-------------------------BD-------------------------------
from config.database import Session
from models.movie import Movie as MovieModel  #tabla
from fastapi.encoders import jsonable_encoder


from middlewares.jwt_handler import validate_token,create_token

login_router = APIRouter()      






@login_router.post('/login', tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password== "123456":
        token:str=create_token(user.dict())
        return JSONResponse(status_code=200,content=token)
    return JSONResponse(status_code=404,content={"mansaje":"validacion incorrecta"})

@login_router.post('/validar', tags=['auth'])
def validar(token:str):
    return validate_token(token) 