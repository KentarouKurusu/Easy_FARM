from fastapi import FastAPI
from routers import route_todo

app = FastAPI()
app.include_router(route_todo.router)

@app.get("/")
def read_root():
    return "Welcome to Fast API!!!"