from fastapi import APIRouter
from fastapi.responses import JSONResponse

from jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()


@user_router.post('/login', tags=['auth'], response_model=dict, status_code=200)
def login(user: User) -> JSONResponse:
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=400, content={"message": "Credenciales incorrectas"})
