from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from fastapi.security import OAuth2PasswordBearer
from app.utils import decode_token
import os

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid auth')
    try:
        payload = decode_token(token)
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user


@router.post('/', response_model=schemas.TodoOut)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_todo = models.Todo(**todo.dict(), owner_id=current_user.id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.get('/', response_model=List[schemas.TodoOut])
def list_todos(page: int = 1, per_page: int = 10, tag: Optional[str] = None, status: Optional[str] = None, sort: Optional[str] = None, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    q = db.query(models.Todo).filter(models.Todo.owner_id == current_user.id)
    if tag:
        q = q.filter(models.Todo.tags.contains(tag))
    if status:
        q = q.filter(models.Todo.status == status)
    if sort == 'due':
        q = q.order_by(models.Todo.due_date)
    todos = q.offset((page - 1) * per_page).limit(per_page).all()
    return todos


@router.get('/{todo_id}', response_model=schemas.TodoOut)
def get_todo(todo_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail='Not found')
    return todo


@router.put('/{todo_id}', response_model=schemas.TodoOut)
def update_todo(todo_id: int, payload: schemas.TodoCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail='Not found')
    for k, v in payload.dict().items():
        setattr(todo, k, v)
    db.commit()
    db.refresh(todo)
    return todo


@router.delete('/{todo_id}')
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail='Not found')
    db.delete(todo)
    db.commit()
    return {'ok': True}
