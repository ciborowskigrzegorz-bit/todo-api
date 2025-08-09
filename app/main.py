from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, todos, users

# create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title='Todo API - Upgraded')
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(todos.router, prefix='/todos', tags=['todos'])


@app.get('/', tags=['root'])
def root():
    return {'message': 'Todo API is up'}
