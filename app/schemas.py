from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[str] = None
    tags: Optional[str] = None
    priority: Optional[int] = 0
    status: Optional[str] = 'todo'


class TodoCreate(TodoBase):
    pass


class TodoOut(TodoBase):
    id: int
    owner_id: int
    done: bool

    model_config = ConfigDict(from_attributes=True)
