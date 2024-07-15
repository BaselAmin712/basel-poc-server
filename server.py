from fastapi import FastAPI
from routers import route

server = FastAPI()

server.include_router(route.router)

@server.get("/")
def root():
    return {"Hello": "World"}