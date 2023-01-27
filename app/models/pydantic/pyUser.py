from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class CreateUser(User):
    pass

class BaseUser(User):
    id: int

    class Config:
        orm_mode = True