from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    class Config:
        orm_mode = True

class ToDoBase(BaseModel):
    title: str
    description: str

class ToDoCreate(ToDoBase):
    pass

class ToDoUpdate(ToDoBase):
    completed: bool

class ToDoOut(ToDoBase):
    id: int
    completed: bool
    class Config:
        orm_mode = True
