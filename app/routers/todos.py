from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ToDoOut)
def create(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo, user_id=1)

@router.get("/", response_model=list[schemas.ToDoOut])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_user_todos(db, user_id=1)
