from fastapi import FastAPI
from app.routers import users, todos

app = FastAPI(title="To-Do List API")

app.include_router(users.router, prefix="/auth", tags=["Auth"])
app.include_router(todos.router, prefix="/todos", tags=["ToDos"])
