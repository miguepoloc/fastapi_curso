from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.database import Base, engine
from middlewares.error_handler import ErrorHandler
from routers.authentication import authentication_router
from routers.movie import movie_router

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(authentication_router)

Base.metadata.create_all(bind=engine)


@app.get('/', tags=['home'])
def message() -> HTMLResponse:
    return HTMLResponse('<h1>Hello world</h1>')
