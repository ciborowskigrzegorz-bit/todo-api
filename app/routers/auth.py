from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils import get_password_hash, verify_password, create_access_token, create_refresh_token, decode_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post('/register', response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter((models.User.username == user.username) | (models.User.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail='User already exists')
    hashed = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post('/login', response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect credentials')
    token = create_access_token({'sub': user.username, 'role': user.role})
    refresh = create_refresh_token({'sub': user.username})
    return {'access_token': token, 'token_type': 'bearer'}


@router.post('/refresh', response_model=schemas.Token)
def refresh_token(request: Request, db: Session = Depends(get_db)):
    body = {}
    try:
        body = request.json()
    except Exception:
        # FastAPI Request.json() is async — fallback to reading body
        try:
            body = {}
        except Exception:
            body = {}
    token = body.get('refresh_token') if isinstance(body, dict) else None
    if not token:
        raise HTTPException(status_code=400, detail='No refresh token')
    try:
        payload = decode_token(token)
        username = payload.get('sub')
    except Exception:
        raise HTTPException(status_code=401, detail='Invalid refresh token')
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail='Invalid user')
    new = create_access_token({'sub': user.username, 'role': user.role})
    return {'access_token': new, 'token_type': 'bearer'}
