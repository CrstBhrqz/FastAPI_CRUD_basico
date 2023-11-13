from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request
from utils.jwt_manager import create_token,validate_token

class JWTBearer(HTTPBearer):#clase para validacion de token en los distintas peticiones de las urls
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403,detail="credenciales son ivalidas")

