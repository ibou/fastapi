from fastapi import Depends, FastAPI, Response, status, HTTPException
from sqlalchemy.orm import Session

from fastapi.params import Body
from typing import Optional
import psycopg
import time
from . import models, schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.get("/")
def root():
    return {"message": "Hello guys"}


@app.get("/posts", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
#   use insert into with placeholders
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    # post = cursor.fetchone() 
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id : {id} was not found",
        )
    return post


@app.get("/posts/recents/latest")
def get_lastest_post():
    return {"lastest_post": my_posts[-1]}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s returning id """, (id,))
    # deleted_post = cursor.fetchone()
    # connection.commit()
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id : {id} was not found",
        )
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s
    #                WHERE id = %s returning * """, (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # connection.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id : {id} was not found.",
        )

    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit() 
    return post_query.first()


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #   use insert into with placeholders
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
