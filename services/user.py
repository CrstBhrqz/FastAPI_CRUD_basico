from schemas.user import User


class UserService():

    def __init__(self,db) -> None: #constructor
        self.db = db

    # def login(self,user:User):
    #     if user.email == "admin@gmail.com" and user.password== "123456":
    #         token:str=create_token(user.dict())
    #         return JSONResponse(status_code=200,content=token)
    #     return JSONResponse(status_code=404,content={"mansaje":"validacion incorrecta"})

    
    # def validar(token:str):
    #     return validate_token(token) 