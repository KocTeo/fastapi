from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int | None = None


    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # def __str__(self):
    #     return f'name': {self.name} + 'age':{se   lf.age}

    # def getDict(self):
    #     new_user = dict(zip(self.name,self.age))

# app = FastAPI()


# @app.post("/user")
# def create_user(user: User):
#     return user
