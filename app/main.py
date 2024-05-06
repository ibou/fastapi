from fastapi import Depends, FastAPI, Response, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.params import Body
from typing import Optional
import psycopg
import time
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




try:
    connection = psycopg.connect(
        "dbname=fastapi user=postgres password=root host=localhost port=5432"
    )
    cursor = connection.cursor()
    print("Connection to PostgreSQL DB successful..")
    
except Exception as e:
    print(f"The error '{e}' occurred.")
    time.sleep(10)


my_posts = [
    {
        "id": 1,
        "title": "Hello title 1",
        "content": "This is a post 1",
        "published": True,
        "rating": 1,
    },
    {
        "id": 2,
        "title": "Hello title 2",
        "content": "This is a post 2 and I like pizza",
        "published": True,
        "rating": 2,
    },
    {
        "id": 3,
        "title": "Hello title 3",
        "content": "This is a post 3 and I like pizza",
        "published": True,
        "rating": 3,
    },
    {
        "id": 4,
        "title": "Hello title 4",
        "content": "This is a post 4 and I like pizza",
        "published": True,
        "rating": 4,
    },
    {
        "id": 5,
        "title": "Hello title 5",
        "content": "This is a post 5 and I like pizza",
        "published": True,
        "rating": 5,
    },
]

def find_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            return post


def find_index_post(id: int):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello guys"}
