from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from fastapi.security import OAuth2PasswordBearer
from app.utils import decode_token

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


@router.get('/me', response_model=schemas.UserOut)
def me(current_user: models.User = Depends(get_current_user)):
    return current_user
