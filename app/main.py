from typing import Union

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.pydantic.pyUser import CreateUser, BaseUser 
from models.slqAlchemy.sqlUser import User

app = FastAPI()

@app.get("/")
def home():
    return { "message": "home" }

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user")
def create_user(user: CreateUser, db: Session=Depends(get_db)):
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users", response_model=list[BaseUser])
def get_users(db: Session=Depends(get_db)):
    return db.query(User).all()