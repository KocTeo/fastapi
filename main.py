from typing import Union

from fastapi import FastAPI

from database.save import save
from models.User import User

import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/user")
def create_user(user: User):
    save(user)
    return user
# pd.DataFrame()
@app.get('/users')
def list_users():
    # data = 'database/data.csv'
    df = pd.read_csv('database/data.csv', sep=";")
    # print(pd.DataFrame(data, index = ''))   
    for i in range(len(df)):
        if i > 0:
            print(dict(df.loc[i]))