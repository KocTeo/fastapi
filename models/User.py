from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int | None = None